import React, { useState } from "react";
import axios from "axios";

function Chatbox() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const handleSendMessage = async () => {
    if (input) {
      // Add the user's message to the state
      setMessages((prevMessages) => [
        ...prevMessages,
        { text: input, sender: "user" },
      ]);
      setInput(""); // Clear the input field

      try {
        // Send the message to the backend with the format { "message": "..." }
        const response = await axios.post("http://localhost:8000/chatbot", {
          message: input, // Send the message as part of the payload
        });

        // Receive the bot's response
        const botResponse = response.data.reply;

        // Add the bot's response to the state
        setMessages((prevMessages) => [
          ...prevMessages,
          { text: botResponse, sender: "bot" },
        ]);
      } catch (error) {
        console.error("Error:", error);
      }
    }
  };

  return (
    <div className="chatbox">
      <div className="chatbox-header">
        <h2>Mental Health Chatbot</h2>
      </div>
      <div className="chatbox-messages">
        {messages.map((msg, index) => (
          <div key={index} className={msg.sender}>
            <p>{msg.text}</p>
          </div>
        ))}
      </div>
      <div className="chatbox-input">
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          placeholder="Type a message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
}

export default Chatbox;
