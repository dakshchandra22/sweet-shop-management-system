import React, { useState } from 'react';
import { useSweet } from '../contexts/SweetContext';
import SweetForm from './SweetForm';
import SweetList from './SweetList';
import './AdminPanel.css';

const AdminPanel = () => {
  const { loading, error } = useSweet();
  const [showForm, setShowForm] = useState(false);
  const [editingSweet, setEditingSweet] = useState(null);

  const handleEdit = (sweet) => {
    setEditingSweet(sweet);
    setShowForm(true);
  };

  const handleFormClose = () => {
    setShowForm(false);
    setEditingSweet(null);
  };

  if (loading) {
    return (
      <div className="admin-panel">
        <div className="loading">Loading admin panel...</div>
      </div>
    );
  }

  return (
    <div className="admin-panel">
      <div className="admin-header">
        <h1>Admin Panel 🛠️</h1>
        <p>Manage your sweet shop inventory</p>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <div className="admin-actions">
        <button 
          onClick={() => setShowForm(true)}
          className="add-button"
        >
          Add New Sweet
        </button>
      </div>

      {showForm && (
        <div className="modal-overlay">
          <div className="modal">
            <SweetForm 
              sweet={editingSweet}
              onClose={handleFormClose}
            />
          </div>
        </div>
      )}

      <SweetList onEdit={handleEdit} />
    </div>
  );
};

export default AdminPanel;
