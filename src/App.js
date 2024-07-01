import React from 'react';
import Layout from './components/Layout';
import ChatInterface from './components/ChatInterface';

function App() {
  return (
    <Layout>
      <div className="h-full flex flex-col">
        <h1 className="text-2xl font-bold p-4">AI Messaging Interface</h1>
        <div className="flex-1">
          <ChatInterface />
        </div>
      </div>
    </Layout>
  );
}

export default App;