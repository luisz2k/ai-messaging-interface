import React from 'react';
import { Code, FileText, Layout } from 'lucide-react';

const ArtifactDisplay = () => {
  return (
    <div className="w-1/3 bg-gray-200 p-4 overflow-y-auto">
      <h2 className="text-lg font-bold mb-4">Generated Content</h2>
      <div className="bg-white rounded p-4 mb-4 flex items-center">
        <Code className="mr-2" /> <span>Code Snippet</span>
      </div>
      <div className="bg-white rounded p-4 mb-4 flex items-center">
        <FileText className="mr-2" /> <span>Text Document</span>
      </div>
      <div className="bg-white rounded p-4 flex items-center">
        <Layout className="mr-2" /> <span>Website Design</span>
      </div>
    </div>
  );
};

export default ArtifactDisplay;