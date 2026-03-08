import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import toast from 'react-hot-toast';

const Auth = ({ isLogin }) => {
    const [form, setForm] = useState({ username: '', email: '', password: '' });
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const endpoint = isLogin ? '/api/auth/login' : '/api/auth/register';
        try {
            const res = await axios.post(`http://localhost:5000${endpoint}`, form);
            if (isLogin) {
                localStorage.setItem('token', res.data.access_token);
                toast.success("Welcome back!");
                navigate('/gallery');
            } else {
                toast.success("Account created! Please sign in.");
                navigate('/login');
            }
        } catch (err) { toast.error("Authentication failed"); }
    };

    return (
        <div className="flex h-screen items-center justify-center bg-slate-50 p-6">
            <div className="w-full max-w-md bg-white p-10 rounded-3xl shadow-xl border border-slate-100">
                <h2 className="text-3xl font-black text-slate-900 mb-8">{isLogin ? 'Sign In' : 'Join Drishyamitra'}</h2>
                <form onSubmit={handleSubmit} className="space-y-4">
                    <input className="w-full p-4 bg-slate-50 border rounded-xl" placeholder="Username" onChange={e => setForm({...form, username: e.target.value})} />
                    {!isLogin && <input className="w-full p-4 bg-slate-50 border rounded-xl" placeholder="Email" onChange={e => setForm({...form, email: e.target.value})} />}
                    <input className="w-full p-4 bg-slate-50 border rounded-xl" type="password" placeholder="Password" onChange={e => setForm({...form, password: e.target.value})} />
                    <button className="w-full bg-indigo-600 text-white p-4 rounded-xl font-bold shadow-lg">Proceed</button>
                </form>
            </div>
        </div>
    );
};

export default Auth;