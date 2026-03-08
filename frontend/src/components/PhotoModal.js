import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { X, UserCheck, Tag } from 'lucide-react';
import axios from 'axios';

const PhotoModal = ({ photo, onClose }) => {
    const [labelName, setLabelName] = useState('');
    const token = localStorage.getItem('token');

    const handleLabel = async (faceId) => {
        try {
            await axios.post(`http://localhost:5000/api/people/label`, 
                { face_id: faceId, name: labelName },
                { headers: { Authorization: `Bearer ${token}` }}
            );
            alert("Face labeled successfully!");
            onClose();
        } catch (err) { alert("Labeling failed"); }
    };

    if (!photo) return null;

    return (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 p-4">
            <motion.div initial={{ scale: 0.9 }} animate={{ scale: 1 }} className="bg-white rounded-3xl overflow-hidden max-w-5xl w-full max-h-[90vh] flex flex-col md:flex-row">
                {/* Image Section with Overlay */}
                <div className="relative bg-slate-900 flex-1 flex items-center justify-center overflow-hidden">
                    <img src={`http://localhost:5000/uploads/${photo.filename}`} alt="Detail" className="max-h-full object-contain" />
                    
                    {/* Face Bounding Boxes */}
                    {photo.faces?.map((face, index) => {
                        const box = JSON.parse(face.location_data);
                        // DeepFace returns [y, x, w, h] or [top, right, bottom, left]
                        return (
                            <div key={index} className="absolute border-2 border-indigo-400 group cursor-help shadow-[0_0_10px_rgba(79,70,229,0.5)]"
                                style={{ top: `${box.y}px`, left: `${box.x}px`, width: `${box.w}px`, height: `${box.h}px` }}>
                                <div className="absolute -top-8 left-0 bg-indigo-600 text-white text-[10px] px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition-opacity whitespace-nowrap">
                                    {face.identity?.name || "Unknown Individual"}
                                </div>
                            </div>
                        );
                    })}
                </div>

                {/* Sidebar Info */}
                <div className="w-full md:w-80 p-6 flex flex-col bg-white">
                    <div className="flex justify-between items-start mb-6">
                        <h3 className="font-bold text-xl text-slate-800">Photo Details</h3>
                        <button onClick={onClose} className="p-2 hover:bg-slate-100 rounded-full"><X size={20}/></button>
                    </div>

                    <div className="space-y-4 flex-1">
                        <div>
                            <p className="text-xs font-bold text-slate-400 uppercase">Recognized People</p>
                            <div className="mt-2 space-y-2">
                                {photo.faces?.map((f, i) => (
                                    <div key={i} className="flex items-center space-x-2 bg-slate-50 p-3 rounded-xl border border-slate-100">
                                        <UserCheck size={16} className="text-indigo-600" />
                                        <span className="text-sm font-medium">{f.identity?.name || "Unknown"}</span>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <div className="pt-4 border-t border-slate-100">
                            <p className="text-xs font-bold text-slate-400 uppercase mb-2">Manual Labeling</p>
                            <input value={labelName} onChange={(e) => setLabelName(e.target.value)} placeholder="Enter name..." className="w-full p-3 bg-slate-50 rounded-xl border border-slate-200 text-sm mb-2 outline-none focus:border-indigo-500" />
                            <button onClick={() => handleLabel(photo.faces[0]?.id)} className="w-full bg-slate-900 text-white p-3 rounded-xl text-sm font-bold flex items-center justify-center space-x-2">
                                <Tag size={16} /> <span>Assign Name</span>
                            </button>
                        </div>
                    </div>
                </div>
            </motion.div>
        </div>
    );
};

export default PhotoModal;