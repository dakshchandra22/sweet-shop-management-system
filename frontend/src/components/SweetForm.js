import React, { useState, useEffect } from 'react';
import { useSweet } from '../contexts/SweetContext';
import './SweetForm.css';

const SweetForm = ({ sweet, onClose }) => {
  const { createSweet, updateSweet } = useSweet();
  const [formData, setFormData] = useState({
    name: '',
    category: '',
    price: '',
    quantity: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    if (sweet) {
      setFormData({
        name: sweet.name,
        category: sweet.category,
        price: sweet.price.toString(),
        quantity: sweet.quantity.toString()
      });
    }
  }, [sweet]);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    const sweetData = {
      ...formData,
      price: parseFloat(formData.price),
      quantity: parseInt(formData.quantity)
    };

    const result = sweet 
      ? await updateSweet(sweet.id, sweetData)
      : await createSweet(sweetData);

    if (result.success) {
      onClose();
    } else {
      setError(result.error);
    }

    setLoading(false);
  };

  return (
    <div className="sweet-form">
      <div className="form-header">
        <h2>{sweet ? 'Edit Sweet' : 'Add New Sweet'}</h2>
        <button onClick={onClose} className="close-button">×</button>
      </div>

      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            className="form-input"
          />
        </div>

        <div className="form-group">
          <label htmlFor="category">Category</label>
          <input
            type="text"
            id="category"
            name="category"
            value={formData.category}
            onChange={handleChange}
            required
            className="form-input"
          />
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="price">Price ($)</label>
            <input
              type="number"
              id="price"
              name="price"
              value={formData.price}
              onChange={handleChange}
              required
              min="0"
              step="0.01"
              className="form-input"
            />
          </div>

          <div className="form-group">
            <label htmlFor="quantity">Quantity</label>
            <input
              type="number"
              id="quantity"
              name="quantity"
              value={formData.quantity}
              onChange={handleChange}
              required
              min="0"
              className="form-input"
            />
          </div>
        </div>

        {error && <div className="error-message">{error}</div>}

        <div className="form-actions">
          <button type="button" onClick={onClose} className="cancel-button">
            Cancel
          </button>
          <button 
            type="submit" 
            disabled={loading}
            className="submit-button"
          >
            {loading ? 'Saving...' : (sweet ? 'Update' : 'Create')}
          </button>
        </div>
      </form>
    </div>
  );
};

export default SweetForm;
