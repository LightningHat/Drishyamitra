import React, { useState, useEffect, useRef } from 'react';
import { MessageSquare, Send, X, Bot, User, Mic, Image as ImageIcon, CheckCircle } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import { useVoiceInput } from '../hooks/useVoiceInput';

const ChatAssistant = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState(JSON.parse(localStorage.getItem('chat_history')) || [
        { role: 'bot', text: 'Hello! I am Drishyamitra. I can help you find photos or share them with contacts. Try "Show me photos of Priya"' }
    ]);
    const [isTyping, setIsTyping] = useState(false);
    const scrollRef = useRef(null);

    // Persistence: Save chat to local storage
    useEffect(() => {
        localStorage.setItem('chat_history', JSON.stringify(messages));
        scrollRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const { isListening, startListening } = useVoiceInput((text) => setInput(text));

    const handleSend = async (textOverride = null) => {
        const query = textOverride || input;
        if (!query.trim()) return;

        const newMsgs = [...messages, { role: 'user', text: query }];
        setMessages(newMsgs);
        setInput('');
        setIsTyping(true);

        try {
            const token = localStorage.getItem('token');
            const res = await axios.post('http://localhost:5000/api/chat/ask', 
                { query }, 
                { headers: { Authorization: `Bearer ${token}` }}
            );

            // Handle Dynamic Results (Thumbnails or Confirmations)
            const botResponse = { 
                role: 'bot', 
                text: res.data.answer,
                results: res.data.intent // structured data from Milestone 3.2
            };
            
            setMessages([...newMsgs, botResponse]);
        } catch (err) {
            setMessages([...newMsgs, { role: 'bot', text: 'Connection lost. Is the backend running?' }]);
        } finally {
            setIsTyping(false);
        }
    };

    return (
        <div className="fixed bottom-6 right-6 z-50">
            <AnimatePresence>
                {isOpen && (
                    <motion.div 
                        initial={{ opacity: 0, scale: 0.8, y: 20 }}
                        animate={{ opacity: 1, scale: 1, y: 0 }}
                        exit={{ opacity: 0, scale: 0.8, y: 20 }}
                        className="bg-white w-96 h-[500px] rounded-3xl shadow-2xl border border-slate-200 flex flex-col overflow-hidden mb-4"
                    >
                        {/* Header */}
                        <div className="bg-indigo-600 p-4 flex justify-between items-center text-white">
                            <div className="flex items-center space-x-2">
                                <Bot size={20} />
                                <span className="font-bold">AI Assistant</span>
                            </div>
                            <button onClick={() => setIsOpen(false)}><X size={20}/></button>
                        </div>

                        {/* Messages */}
                        <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-slate-50">
                            {messages.map((m, i) => (
                                <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                                    <div className={`max-w-[85%] p-3 rounded-2xl text-sm shadow-sm ${
                                        m.role === 'user' ? 'bg-indigo-600 text-white rounded-br-none' : 'bg-white text-slate-800 rounded-bl-none'
                                    }`}>
                                        <div className="flex items-start space-x-2">
                                            {m.role === 'bot' && <Bot size={14} className="mt-1 shrink-0 text-indigo-600" />}
                                            <p>{m.text}</p>
                                        </div>
                                        
                                        {/* Dynamic Photo Previews (if AI finds something) */}
                                        {m.results?.action === 'search' && (
                                            <div className="mt-3 flex space-x-2 overflow-x-auto pb-2">
                                                <div className="w-16 h-16 bg-slate-200 rounded-lg flex items-center justify-center">
                                                    <ImageIcon size={16} className="text-slate-400" />
                                                </div>
                                                <div className="text-[10px] text-indigo-600 font-bold self-center">Fetching...</div>
                                            </div>
                                        )}
                                    </div>
                                </div>
                            ))}
                            {isTyping && (
                                <div className="flex space-x-1 p-2 bg-slate-200 w-12 rounded-full justify-center">
                                    <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce" />
                                    <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce delay-75" />
                                    <div className="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce delay-150" />
                                </div>
                            )}
                            <div ref={scrollRef} />
                        </div>

                        {/* Input */}
                        <div className="p-3 border-t flex items-center space-x-2 bg-white">
                            <button 
                                onClick={startListening}
                                className={`p-2 rounded-full ${isListening ? 'bg-red-100 text-red-600' : 'text-slate-400 hover:bg-slate-100'}`}
                            >
                                <Mic size={20} />
                            </button>
                            <input 
                                value={input}
                                onChange={(e) => setInput(e.target.value)}
                                onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                                placeholder="Type a message..."
                                className="flex-1 text-sm outline-none"
                            />
                            <button onClick={() => handleSend()} className="p-2 text-indigo-600 hover:bg-indigo-50 rounded-full">
                                <Send size={20} />
                            </button>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Toggle Button */}
            <motion.button 
                whileHover={{ scale: 1.1 }}
                whileTap={{ scale: 0.9 }}
                onClick={() => setIsOpen(!isOpen)}
                className="bg-indigo-600 text-white p-4 rounded-full shadow-2xl flex items-center justify-center"
            >
                {isOpen ? <X size={28} /> : <MessageSquare size={28} />}
            </motion.button>
        </div>
    );
};

export default ChatAssistant;