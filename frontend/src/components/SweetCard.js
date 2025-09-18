import React, { useState } from 'react';
import { useSweet } from '../contexts/SweetContext';
import './SweetCard.css';

const SweetCard = ({ sweet }) => {
  const [quantity, setQuantity] = useState(1);
  const [message, setMessage] = useState('');
  const { purchaseSweet } = useSweet();

  const handlePurchase = async () => {
    // Ensure quantity is a valid number
    const purchaseQuantity = parseInt(quantity) || 1;
    
    if (purchaseQuantity > sweet.quantity) {
      setMessage('Not enough in stock!');
      return;
    }

    if (purchaseQuantity <= 0) {
      setMessage('Please enter a valid quantity!');
      return;
    }

    const result = await purchaseSweet(sweet.id, purchaseQuantity);
    
    if (result.success) {
      setMessage(`Successfully purchased ${purchaseQuantity} ${sweet.name}(s)!`);
      setQuantity(1);
    } else {
      setMessage(result.error || 'Purchase failed');
    }

    // Clear message after 3 seconds
    setTimeout(() => setMessage(''), 3000);
  };

  return (
    <div className="sweet-card">
      <div className="sweet-image">
        <span className="sweet-emoji">🍭</span>
      </div>
      
      <div className="sweet-info">
        <h3 className="sweet-name">{sweet.name}</h3>
        <p className="sweet-category">{sweet.category}</p>
        <p className="sweet-price">${sweet.price.toFixed(2)}</p>
        <p className="sweet-quantity">
          {sweet.quantity > 0 ? `${sweet.quantity} in stock` : 'Out of stock'}
        </p>
      </div>

      <div className="sweet-actions">
        <div className="quantity-controls">
          <label htmlFor={`quantity-${sweet.id}`}>Quantity:</label>
          <input
            type="number"
            id={`quantity-${sweet.id}`}
            min="1"
            max={sweet.quantity}
            value={quantity}
            onChange={(e) => {
              const inputValue = e.target.value;
              
              if (inputValue === '') {
                setQuantity(1);
              } else {
                const value = parseInt(inputValue);
                if (!isNaN(value) && value > 0) {
                  setQuantity(value);
                }
              }
            }}
            className="quantity-input"
            disabled={sweet.quantity === 0}
          />
          <span className="quantity-display">(Current: {quantity})</span>
        </div>

        <button
          onClick={handlePurchase}
          disabled={sweet.quantity === 0}
          className={`purchase-button ${sweet.quantity === 0 ? 'disabled' : ''}`}
        >
          {sweet.quantity === 0 ? 'Out of Stock' : 'Purchase'}
        </button>

        {message && (
          <div className={`message ${message.includes('Successfully') ? 'success' : 'error'}`}>
            {message}
          </div>
        )}
      </div>
    </div>
  );
};

export default SweetCard;
