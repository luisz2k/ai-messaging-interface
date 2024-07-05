import React from 'react';
import Layout from './components/Layout';
import ChatInterface from './components/ChatInterface';
import ArtifactDisplay from './components/ArtifactDisplay';

function App() {
  return (
    <Layout>
      <div className="flex-1 flex">
        <ChatInterface />
        <ArtifactDisplay />
      </div>
    </Layout>
  );
}

export default App;