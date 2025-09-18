import React from 'react';
import { useSweet } from '../contexts/SweetContext';
import SweetCard from './SweetCard';
import SearchBar from './SearchBar';
import './Dashboard.css';

const Dashboard = () => {
  const { sweets, loading, error, searchSweets, fetchSweets } = useSweet();

  const handleSearch = (params) => {
    if (Object.values(params).some(value => value !== '')) {
      searchSweets(params);
    } else {
      fetchSweets();
    }
  };

  const handleClearSearch = () => {
    fetchSweets();
  };

  if (loading) {
    return (
      <div className="dashboard">
        <div className="loading">Loading sweets...</div>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Welcome to Sweet Shop! 🍭</h1>
        <p>Discover our delicious collection of sweets</p>
      </div>

      <SearchBar onSearch={handleSearch} onClear={handleClearSearch} />

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      <div className="sweets-grid">
        {sweets.length === 0 ? (
          <div className="no-sweets">
            <h3>No sweets found</h3>
            <p>Try adjusting your search criteria</p>
          </div>
        ) : (
          sweets.map(sweet => (
            <SweetCard key={sweet.id} sweet={sweet} />
          ))
        )}
      </div>
    </div>
  );
};

export default Dashboard;
