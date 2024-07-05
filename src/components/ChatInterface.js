import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChatInterface = () => {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');

  const handleSendMessage = async () => {
    if (inputMessage.trim() === '') return;

    const newMessage = { text: inputMessage, sender: 'user' };
    setMessages([...messages, newMessage]);
    setInputMessage('');

    try {
      const response = await axios.post('http://localhost:5000/chat', { message: inputMessage });
      setMessages(prevMessages => [...prevMessages, { text: response.data.response, sender: 'ai' }]);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <div className="flex-1 flex flex-col">
      {/* Chat Messages */}
      <div className="flex-1 bg-white p-4 overflow-y-auto">
        {messages.map((message, index) => (
          <div key={index} className={`mb-4 p-2 rounded-lg ${message.sender === 'user' ? 'bg-blue-100' : 'bg-green-100'}`}>
            {message.text}
          </div>
        ))}
      </div>

      {/* Message Input */}
      <div className="bg-white p-4 border-t">
        <div className="flex">
          <input
            className="flex-1 border rounded-l px-2 py-1"
            placeholder="Type your message..."
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          />
          <button
            className="bg-blue-500 text-white px-4 py-1 rounded-r"
            onClick={handleSendMessage}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;