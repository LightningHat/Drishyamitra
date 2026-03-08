import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Layout from './components/Layout';
import Login from './pages/Login';

// Optimized: Code Splitting (Lazy Loading)
const Gallery = lazy(() => import('./pages/Gallery'));
const Chatbot = lazy(() => import('./pages/Chatbot'));

// Loading Screen for Suspense
const Loader = () => (
    <div className="h-screen flex items-center justify-center bg-slate-50">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
    </div>
);

const Placeholder = ({ name }) => (
    <div className="bg-white p-20 rounded-3xl border-2 border-dashed border-slate-200 text-center">
        <h2 className="text-2xl font-bold text-slate-400 mb-2">{name}</h2>
        <p className="text-slate-300 font-medium text-sm">System ready for production deployment.</p>
    </div>
);

function App() {
  const isAuthenticated = () => !!localStorage.getItem('token');

  return (
    <Router>
      <Toaster position="top-right" reverseOrder={false} />
      
      {/* Suspense handles the loading state of lazy-loaded modules */}
      <Suspense fallback={<Loader />}>
        <Routes>
          <Route path="/login" element={<Login />} />
          
          <Route path="/gallery" element={isAuthenticated() ? <Layout><Gallery /></Layout> : <Navigate to="/login" />} />
          <Route path="/chat" element={isAuthenticated() ? <Layout><Chatbot /></Layout> : <Navigate to="/login" />} />
          <Route path="/people" element={isAuthenticated() ? <Layout><Placeholder name="People Management" /></Layout> : <Navigate to="/login" />} />
          <Route path="/history" element={isAuthenticated() ? <Layout><Placeholder name="Delivery History" /></Layout> : <Navigate to="/login" />} />
          
          <Route path="/" element={<Navigate to="/gallery" />} />
        </Routes>
      </Suspense>
    </Router>
  );
}

export default App;