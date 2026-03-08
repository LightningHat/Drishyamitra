import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';
import { Upload, Filter, Search, Maximize2 } from 'lucide-react';
import PhotoModal from '../components/PhotoModal';

const Gallery = () => {
    const [photos, setPhotos] = useState([]);
    const [selectedPhoto, setSelectedPhoto] = useState(null);
    const [filter, setFilter] = useState('all');
    const token = localStorage.getItem('token');

    useEffect(() => { fetchPhotos(); }, []);

    const fetchPhotos = async () => {
        try {
            const res = await axios.get('http://localhost:5000/api/photos', {
                headers: { Authorization: `Bearer ${token}` }
            });
            setPhotos(res.data);
        } catch (err) { console.error("Fetch failed"); }
    };

    const handleFileUpload = async (e) => {
        const files = Array.from(e.target.files);
        const formData = new FormData();
        files.forEach(file => formData.append('file', file));

        try {
            await axios.post('http://localhost:5000/api/photos/upload', formData, {
                headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data' }
            });
            alert("Upload successful! AI is processing...");
            fetchPhotos();
        } catch (err) { alert("Upload failed"); }
    };

    return (
        <div className="space-y-8">
            {/* Header with Actions */}
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <h2 className="text-3xl font-extrabold text-slate-900 tracking-tight">Your Memories</h2>
                    <p className="text-slate-500 text-sm">Organized automatically by AI</p>
                </div>
                
                <div className="flex items-center space-x-3">
                    <div className="relative">
                        <Search className="absolute left-3 top-2.5 text-slate-400" size={18} />
                        <input placeholder="Search people..." className="pl-10 pr-4 py-2 bg-white border border-slate-200 rounded-xl text-sm outline-none focus:border-indigo-500 w-64" />
                    </div>
                    <label className="bg-indigo-600 text-white px-5 py-2.5 rounded-xl text-sm font-bold shadow-lg shadow-indigo-100 cursor-pointer hover:bg-indigo-700 transition-all flex items-center space-x-2">
                        <Upload size={18} />
                        <span>Upload Photos</span>
                        <input type="file" multiple hidden onChange={handleFileUpload} />
                    </label>
                </div>
            </div>

            {/* Grid */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                {photos.map((photo) => (
                    <motion.div key={photo.id} whileHover={{ y: -5 }} className="bg-white rounded-3xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-xl transition-all cursor-pointer group" onClick={() => setSelectedPhoto(photo)}>
                        <div className="aspect-square bg-slate-100 relative overflow-hidden">
                            <img src={`http://localhost:5000/uploads/${photo.filename}`} className="w-full h-full object-cover" alt="Gallery item" />
                            <div className="absolute inset-0 bg-indigo-900/20 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                                <Maximize2 className="text-white" />
                            </div>
                        </div>
                        <div className="p-4">
                            <p className="text-xs font-bold text-indigo-600 uppercase tracking-widest mb-1">
                                {photo.faces?.length > 0 ? `${photo.faces.length} Faces Detected` : "Processing..."}
                            </p>
                            <h4 className="text-sm font-bold text-slate-800 truncate">{photo.filename}</h4>
                        </div>
                    </motion.div>
                ))}
            </div>

            {/* Photo Detail Modal */}
            <PhotoModal photo={selectedPhoto} onClose={() => setSelectedPhoto(null)} />
        </div>
    );
};

export default Gallery;