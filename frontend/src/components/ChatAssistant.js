import React, { useState, useEffect, useRef } from 'react';
import { MessageSquare, Send, X, Bot, Mic } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import axios from 'axios';
import toast from 'react-hot-toast';

const ChatAssistant = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([{ role: 'bot', text: 'Hi! I am Drishyamitra. Try asking "Who is in my photos?"' }]);
    const [isTyping, setIsTyping] = useState(false);
    const scrollRef = useRef(null);

    useEffect(() => { scrollRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages]);

    const handleSend = async () => {
        if (!input.trim()) return;
        const newMsgs = [...messages, { role: 'user', text: input }];
        setMessages(newMsgs);
        setInput('');
        setIsTyping(true);

        try {
            const token = localStorage.getItem('token');
            const res = await axios.post('http://localhost:5000/api/chat/ask', 
                { query: input }, 
                { headers: { Authorization: `Bearer ${token}` }}
            );
            setMessages([...newMsgs, { role: 'bot', text: res.data.answer }]);
        } catch (err) {
            toast.error("AI service currently offline.");
        } finally {
            setIsTyping(false);
        }
    };

    return (
        <div className="fixed bottom-6 right-6 z-50">
            <AnimatePresence>
                {isOpen && (
                    <motion.div initial={{ opacity: 0, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0, scale: 0.9 }} className="bg-white w-80 h-96 rounded-3xl shadow-2xl border border-slate-200 flex flex-col overflow-hidden mb-4">
                        <div className="bg-indigo-600 p-4 flex justify-between items-center text-white">
                            <span className="font-bold flex items-center"><Bot size={18} className="mr-2"/> AI Assistant</span>
                            <button onClick={() => setIsOpen(false)}><X size={18}/></button>
                        </div>
                        <div className="flex-1 overflow-y-auto p-4 space-y-3 bg-slate-50">
                            {messages.map((m, i) => (
                                <div key={i} className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}>
                                    <div className={`p-3 rounded-2xl text-xs ${m.role === 'user' ? 'bg-indigo-600 text-white' : 'bg-white border text-slate-800'}`}>
                                        {m.text}
                                    </div>
                                </div>
                            ))}
                            {isTyping && <div className="text-slate-400 text-[10px] italic">AI is typing...</div>}
                            <div ref={scrollRef} />
                        </div>
                        <div className="p-2 border-t flex space-x-2 bg-white">
                            <input value={input} onChange={(e) => setInput(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleSend()} className="flex-1 text-sm px-2 outline-none" placeholder="Ask AI..." />
                            <button onClick={handleSend} className="bg-indigo-600 text-white p-2 rounded-xl"><Send size={16} /></button>
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
            <button onClick={() => setIsOpen(!isOpen)} className="bg-indigo-600 text-white p-4 rounded-full shadow-xl">
                <MessageSquare />
            </button>
        </div>
    );
};

export default ChatAssistant;