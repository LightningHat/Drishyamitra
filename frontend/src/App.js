import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Gallery from './pages/Gallery';

const Placeholder = ({ name }) => (
    <div className="bg-white p-20 rounded-3xl border-2 border-dashed border-slate-200 text-center">
        <h2 className="text-2xl font-bold text-slate-400 mb-2">{name}</h2>
        <p className="text-slate-300 font-medium text-sm">Waiting for AI integration...</p>
    </div>
);

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/gallery" />} />
        <Route path="/gallery" element={<Layout><Gallery /></Layout>} />
        <Route path="/chat" element={<Layout><Placeholder name="AI Chatbot Assistant" /></Layout>} />
        <Route path="/people" element={<Layout><Placeholder name="People Management" /></Layout>} />
        <Route path="/history" element={<Layout><Placeholder name="Delivery History Tracking" /></Layout>} />
      </Routes>
    </Router>
  );
}

export default App;