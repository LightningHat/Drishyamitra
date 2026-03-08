import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import { Upload, Maximize2, RefreshCcw } from 'lucide-react';
import toast from 'react-hot-toast';
import PhotoModal from '../components/PhotoModal';

const Gallery = () => {
    const [photos, setPhotos] = useState([]);
    const [selectedPhoto, setSelectedPhoto] = useState(null);
    const [isRefreshing, setIsRefreshing] = useState(false);
    const token = localStorage.getItem('token');

    useEffect(() => {
        fetchPhotos();
        const interval = setInterval(fetchPhotos, 15000); // Poll every 15s
        return () => clearInterval(interval);
    }, []);

    const fetchPhotos = async () => {
        setIsRefreshing(true);
        try {
            const res = await axios.get('http://localhost:5000/api/photos', {
                headers: { Authorization: `Bearer ${token}` }
            });
            setPhotos(res.data);
        } catch (err) {
            console.error("Gallery sync failed");
        } finally {
            setIsRefreshing(false);
        }
    };

    const handleFileUpload = async (e) => {
        const file = e.target.files[0];
        if (!file) return;

        const formData = new FormData();
        formData.append('file', file);

        const toastId = toast.loading(`Uploading ${file.name}...`);

        try {
            await axios.post('http://localhost:5000/api/photos/upload', formData, {
                headers: { 
                    Authorization: `Bearer ${token}`, 
                    'Content-Type': 'multipart/form-data' 
                },
                onUploadProgress: (p) => {
                    const progress = Math.round((p.loaded * 100) / p.total);
                    toast.loading(`Uploading: ${progress}%`, { id: toastId });
                }
            });
            toast.success("Upload success! AI is thinking...", { id: toastId });
            fetchPhotos();
        } catch (err) {
            toast.error("Upload failed.", { id: toastId });
        }
    };

    return (
        <div className="space-y-8">
            <div className="flex justify-between items-center">
                <div>
                    <h2 className="text-3xl font-extrabold text-slate-900 tracking-tight">Your Memories</h2>
                    <div className="flex items-center text-slate-500 text-sm mt-1">
                        <RefreshCcw size={14} className={`mr-2 ${isRefreshing ? 'animate-spin' : ''}`} />
                        {isRefreshing ? 'AI Syncing...' : 'Synced with Cloud'}
                    </div>
                </div>
                
                <label className="bg-indigo-600 text-white px-6 py-3 rounded-2xl text-sm font-bold shadow-xl cursor-pointer hover:bg-indigo-700 transition-all flex items-center space-x-2">
                    <Upload size={18} />
                    <span>Upload New</span>
                    <input type="file" hidden onChange={handleFileUpload} />
                </label>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                {photos.map((photo) => (
                    <motion.div 
                        key={photo.id} 
                        initial={{ opacity: 0 }} animate={{ opacity: 1 }} whileHover={{ y: -5 }} 
                        className="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-sm cursor-pointer group" 
                        onClick={() => setSelectedPhoto(photo)}
                    >
                        <div className="aspect-square bg-slate-100 relative overflow-hidden">
                            <img src={`http://localhost:5000/uploads/${photo.filename}`} className="w-full h-full object-cover" alt="Memory" />
                            <div className="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                                <Maximize2 className="text-white" />
                            </div>
                        </div>
                        <div className="p-4 flex justify-between items-center">
                            <h4 className="text-sm font-bold text-slate-800 truncate w-32">{photo.filename}</h4>
                            <span className={`text-[9px] px-2 py-0.5 rounded-full font-bold uppercase ${photo.faces?.length > 0 ? 'bg-green-100 text-green-600' : 'bg-amber-100 text-amber-600'}`}>
                                {photo.faces?.length > 0 ? 'Recognized' : 'Processing'}
                            </span>
                        </div>
                    </motion.div>
                ))}
            </div>

            {selectedPhoto && <PhotoModal photo={selectedPhoto} onClose={() => setSelectedPhoto(null)} />}
        </div>
    );
};

export default Gallery;