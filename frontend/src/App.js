import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState("Connecting to backend...");

  useEffect(() => {
    // This uses the URL from your .env file
    const backendUrl = process.env.REACT_APP_API_URL || "http://localhost:5000";
    
    axios.get(`${backendUrl}/api/health`)
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error("Error connecting to backend:", error);
        setMessage("Backend is offline. Make sure start_server.py is running!");
      });
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Drishyamitra AI Project</h1>
      <p>Backend Status: <strong>{message}</strong></p>
      
      {/* We will build the Upload component here next! */}
      <div style={{ border: '1px solid #ccc', padding: '20px', margin: '20px' }}>
        <h3>Photo Upload Section (Coming Soon)</h3>
      </div>
    </div>
  );
}

export default App;