import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Camera, Shield, Zap, ArrowRight } from 'lucide-react';

const Home = () => {
    return (
        <div className="bg-slate-50 min-h-screen">
            <nav className="p-6 flex justify-between items-center max-w-7xl mx-auto">
                <div className="flex items-center space-x-2 font-bold text-2xl text-indigo-600">
                    <Camera /> <span>Drishyamitra</span>
                </div>
                <Link to="/login" className="bg-indigo-600 text-white px-6 py-2 rounded-full font-bold hover:bg-indigo-700 transition-all">
                    Sign In
                </Link>
            </nav>

            <main className="max-w-7xl mx-auto px-6 py-20 text-center">
                <motion.h1 initial={{y:20, opacity:0}} animate={{y:0, opacity:1}} className="text-6xl font-black text-slate-900 mb-6">
                    Memories Managed by <span className="text-indigo-600">Intelligence.</span>
                </motion.h1>
                <p className="text-slate-500 text-xl max-w-2xl mx-auto mb-10">
                    The AI-powered companion that organizes your photos, recognizes your loved ones, and shares memories instantly.
                </p>
                <div className="flex justify-center space-x-4">
                    <Link to="/register" className="bg-slate-900 text-white px-8 py-4 rounded-2xl font-bold flex items-center group shadow-xl">
                        Get Started <ArrowRight className="ml-2 group-hover:translate-x-1 transition-transform" />
                    </Link>
                </div>

                <div className="grid md:grid-cols-3 gap-8 mt-24">
                    <FeatureCard icon={<Zap className="text-amber-500" />} title="Facial Recognition" desc="Powered by Facenet512 and RetinaFace for extreme accuracy." />
                    <FeatureCard icon={<Shield className="text-green-500" />} title="Secure Delivery" desc="Automated photo sharing via WhatsApp and Gmail API." />
                    <FeatureCard icon={<Camera className="text-indigo-500" />} title="Smart Folders" desc="AI automatically categorizes your digital chaos." />
                </div>
            </main>
        </div>
    );
};

const FeatureCard = ({ icon, title, desc }) => (
    <div className="bg-white p-8 rounded-3xl shadow-sm border border-slate-100 text-left">
        <div className="mb-4">{icon}</div>
        <h3 className="font-bold text-lg mb-2">{title}</h3>
        <p className="text-slate-500 text-sm">{desc}</p>
    </div>
);

export default Home;