import React from 'react';
import { motion } from 'framer-motion';
import { Share2, Trash2, Maximize2, Image as ImageIcon, Clock } from 'lucide-react';

const PhotoCard = ({ id }) => (
  <motion.div 
    whileHover={{ y: -4 }}
    className="group bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-xl hover:shadow-slate-200/50 transition-all duration-300"
  >
    <div className="aspect-[4/3] bg-slate-100 relative overflow-hidden">
        <div className="absolute inset-0 flex items-center justify-center text-slate-300">
            <ImageIcon size={48} strokeWidth={1} />
        </div>
        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center opacity-0 group-hover:opacity-100">
            <button className="p-2 bg-white rounded-full text-slate-900 shadow-xl"><Maximize2 size={20}/></button>
        </div>
    </div>
    <div className="p-4">
      <div className="flex justify-between items-start mb-2">
        <div>
          <h4 className="text-sm font-bold text-slate-800">IMG_{id}.jpg</h4>
          <p className="text-[10px] font-bold text-indigo-600 uppercase tracking-tighter">AI Recognized</p>
        </div>
        <div className="flex space-x-1">
          <button className="p-1.5 text-slate-400 hover:text-indigo-600 hover:bg-indigo-50 rounded-lg transition-colors"><Share2 size={14}/></button>
          <button className="p-1.5 text-slate-400 hover:text-red-500 hover:bg-red-50 rounded-lg transition-colors"><Trash2 size={14}/></button>
        </div>
      </div>
      <div className="flex items-center text-[10px] text-slate-400">
        <Clock size={10} className="mr-1"/> Recently processed
      </div>
    </div>
  </motion.div>
);

const Gallery = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-end">
        <div>
            <h2 className="text-3xl font-extrabold text-slate-900 tracking-tight">Memories</h2>
            <p className="text-slate-500 text-sm">Automated organization active</p>
        </div>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {[1, 2, 3, 4, 5, 6, 7, 8].map(i => <PhotoCard key={i} id={i} />)}
      </div>
    </div>
  );
};

export default Gallery;