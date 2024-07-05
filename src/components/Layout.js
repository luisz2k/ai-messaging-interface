import React from 'react';
import { MessageCircle, Upload, Settings } from 'lucide-react';

const Layout = ({ children }) => {
  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-16 bg-gray-800 text-white flex flex-col items-center py-4">
        <button className="p-2 hover:bg-gray-700 rounded mb-4"><MessageCircle /></button>
        <button className="p-2 hover:bg-gray-700 rounded mb-4"><Upload /></button>
        <button className="p-2 hover:bg-gray-700 rounded"><Settings /></button>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex">
        {children}
      </div>
    </div>
  );
};

export default Layout;