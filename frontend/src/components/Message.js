import React from 'react';

const Message = ({ message, onClose }) => {
  if (!message) return null;

  return (
    <div className="message">
      {message}
      <button onClick={onClose} className="close-btn">×</button>
    </div>
  );
};

export default Message;

