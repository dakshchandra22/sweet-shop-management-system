import React, { useState } from 'react';
import { useSweet } from '../contexts/SweetContext';
import './SweetList.css';

const SweetList = ({ onEdit }) => {
  const { sweets, deleteSweet, restockSweet } = useSweet();
  const [restockQuantities, setRestockQuantities] = useState({});

  const handleDelete = async (sweet) => {
    if (window.confirm(`Are you sure you want to delete "${sweet.name}"?`)) {
      await deleteSweet(sweet.id);
    }
  };

  const handleRestock = async (sweetId, quantity) => {
    if (quantity <= 0) {
      alert('Please enter a valid quantity');
      return;
    }

    const result = await restockSweet(sweetId, quantity);
    if (result.success) {
      setRestockQuantities(prev => ({
        ...prev,
        [sweetId]: ''
      }));
    } else {
      alert(result.error);
    }
  };

  const handleRestockQuantityChange = (sweetId, value) => {
    setRestockQuantities(prev => ({
      ...prev,
      [sweetId]: value
    }));
  };

  return (
    <div className="sweet-list">
      <h2>Sweet Inventory</h2>
      
      {sweets.length === 0 ? (
        <div className="no-sweets">
          <p>No sweets in inventory. Add some to get started!</p>
        </div>
      ) : (
        <div className="sweets-table">
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Category</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {sweets.map(sweet => (
                <tr key={sweet.id}>
                  <td className="sweet-name">{sweet.name}</td>
                  <td className="sweet-category">{sweet.category}</td>
                  <td className="sweet-price">${sweet.price.toFixed(2)}</td>
                  <td className="sweet-quantity">
                    <span className={`quantity-badge ${sweet.quantity === 0 ? 'out-of-stock' : ''}`}>
                      {sweet.quantity}
                    </span>
                  </td>
                  <td className="sweet-actions">
                    <div className="action-buttons">
                      <button 
                        onClick={() => onEdit(sweet)}
                        className="edit-button"
                      >
                        Edit
                      </button>
                      
                      <div className="restock-section">
                        <input
                          type="number"
                          min="1"
                          value={restockQuantities[sweet.id] || ''}
                          onChange={(e) => handleRestockQuantityChange(sweet.id, e.target.value)}
                          placeholder="Qty"
                          className="restock-input"
                        />
                        <button
                          onClick={() => handleRestock(sweet.id, parseInt(restockQuantities[sweet.id] || 0))}
                          className="restock-button"
                        >
                          Restock
                        </button>
                      </div>
                      
                      <button 
                        onClick={() => handleDelete(sweet)}
                        className="delete-button"
                      >
                        Delete
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default SweetList;
