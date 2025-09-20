import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useSweet } from '../contexts/SweetContext';
import Header from './Header';
import Login from './Login';
import Register from './Register';
import SearchBar from './SearchBar';
import SweetForm from './SweetForm';
import SweetList from './SweetList';
import Message from './Message';

const SweetShop = () => {
  const { user, logout } = useAuth();
  const { sweets, loading } = useSweet();

  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('');
  const [message, setMessage] = useState('');
  const [editingSweet, setEditingSweet] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [currentPage, setCurrentPage] = useState('login');

  const handleEditSweet = (sweet) => {
    setEditingSweet(sweet);
    setShowModal(true);
  };

  const handleCancelEdit = () => {
    setEditingSweet(null);
    setShowModal(false);
  };

  const handleAuthSuccess = () => {
    setCurrentPage('dashboard');
  };

  const handlePageChange = (page) => {
    setCurrentPage(page);
  };

  const handleAddNew = () => {
    setEditingSweet(null);
    setShowModal(true);
  };

  const handleLogout = () => {
    logout();
    setCurrentPage('login');
  };

  let filteredSweets = sweets.filter(sweet =>
    sweet.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    sweet.category.toLowerCase().includes(searchTerm.toLowerCase())
  );

  if (sortBy === 'low-high') {
    filteredSweets = filteredSweets.sort((a, b) => a.price - b.price);
  } else if (sortBy === 'high-low') {
    filteredSweets = filteredSweets.sort((a, b) => b.price - a.price);
  }

  if (loading) return <div className="loading">Loading...</div>;

  if (!user) {
    if (currentPage === 'login') {
      return <Login onSuccess={handleAuthSuccess} onPageChange={handlePageChange} />;
    } else if (currentPage === 'register') {
      return <Register onSuccess={handleAuthSuccess} onPageChange={handlePageChange} />;
    }
  }

  return (
    <div className="app">
      <Header onPageChange={handlePageChange} onLogout={handleLogout} />
      
      <Message message={message} onClose={() => setMessage('')} />

      <SearchBar 
        searchTerm={searchTerm} 
        onSearchChange={setSearchTerm}
        onAddNew={handleAddNew}
        onSortChange={setSortBy}
      />

      {user?.is_admin && (
        <SweetForm 
          editingSweet={editingSweet} 
          onCancel={handleCancelEdit}
          show={showModal}
        />
      )}

      <SweetList 
        sweets={filteredSweets} 
        onEditSweet={handleEditSweet}
      />
    </div>
  );
};

export default SweetShop;