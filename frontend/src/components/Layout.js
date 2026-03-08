import React from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { Image as ImageIcon, Users, MessageSquare, History, LogOut, LayoutDashboard } from 'lucide-react';
import { motion } from 'framer-motion';
import ChatAssistant from './ChatAssistant';

/**
 * SidebarItem: Helper component for navigation links
 */
const SidebarItem = ({ icon: Icon, label, to, active }) => (
  <Link to={to}>
    <motion.div 
      whileHover={{ x: 4 }}
      whileTap={{ scale: 0.95 }}
      className={`flex items-center space-x-3 p-3 rounded-xl cursor-pointer transition-all ${
        active 
        ? 'bg-indigo-600 text-white shadow-md shadow-indigo-200' 
        : 'text-slate-500 hover:bg-slate-100 hover:text-slate-900'
      }`}
    >
      <Icon size={20} />
      <span className="font-semibold text-sm">{label}</span>
    </motion.div>
  </Link>
);

/**
 * Layout: The main wrapper for the application
 * Includes Sidebar, Top bar, and Floating AI Assistant
 */
const Layout = ({ children }) => {
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.clear();
    navigate('/login');
  };

  return (
    <div className="flex h-screen bg-slate-50 overflow-hidden">
      
      {/* 1. Sidebar Navigation */}
      <aside className="w-64 bg-white border-r border-slate-200 hidden md:flex flex-col p-6 shrink-0">
        <div className="flex items-center space-x-3 mb-10 px-2">
          <div className="w-10 h-10 bg-indigo-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-indigo-100">
            <ImageIcon size={24} />
          </div>
          <h1 className="text-xl font-bold text-slate-800 tracking-tight">Drishyamitra</h1>
        </div>
        
        <nav className="flex-1 space-y-1">
          <SidebarItem icon={LayoutDashboard} label="Dashboard" to="/gallery" active={location.pathname === '/gallery'} />
          <SidebarItem icon={ImageIcon} label="Gallery" to="/gallery" active={location.pathname === '/gallery'} />
          <SidebarItem icon={Users} label="People" to="/people" active={location.pathname === '/people'} />
          <SidebarItem icon={MessageSquare} label="AI Assistant" to="/chat" active={location.pathname === '/chat'} />
          <SidebarItem icon={History} label="History" to="/history" active={location.pathname === '/history'} />
        </nav>

        {/* Logout Button */}
        <button 
          onClick={handleLogout}
          className="flex items-center space-x-3 p-3 text-slate-400 hover:text-red-500 transition-colors mt-auto font-medium text-sm border-t border-slate-50 pt-4"
        >
          <LogOut size={18} />
          <span>Sign Out</span>
        </button>
      </aside>

      {/* 2. Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden relative">
        
        {/* Top Header Bar */}
        <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-8 shrink-0 z-10">
          <div className="text-slate-400 text-sm italic font-medium">
            AI-Powered Photo Management System
          </div>
          <div className="flex items-center space-x-4">
            <button className="bg-indigo-600 text-white px-5 py-2 rounded-xl text-sm font-bold shadow-md shadow-indigo-100 hover:bg-indigo-700 transition-all active:scale-95">
              + Upload New
            </button>
          </div>
        </header>

        {/* Scrollable Page Content */}
        <div className="flex-1 overflow-y-auto p-8 bg-slate-50/50">
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.4 }}
            className="max-w-7xl mx-auto"
          >
            {children}
          </motion.div>
        </div>

        {/* 3. Floating AI Chat Assistant (Milestone 4.2) */}
        <ChatAssistant />

      </main>
    </div>
  );
};

export default Layout;