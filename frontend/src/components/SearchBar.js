import React, { useState } from 'react';
import './SearchBar.css';

const SearchBar = ({ onSearch, onClear }) => {
  const [searchParams, setSearchParams] = useState({
    name: '',
    category: '',
    min_price: '',
    max_price: ''
  });

  const handleChange = (e) => {
    setSearchParams({
      ...searchParams,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(searchParams);
  };

  const handleClear = () => {
    setSearchParams({
      name: '',
      category: '',
      min_price: '',
      max_price: ''
    });
    onClear();
  };

  return (
    <div className="search-bar">
      <form onSubmit={handleSubmit} className="search-form">
        <div className="search-row">
          <div className="search-field">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              name="name"
              value={searchParams.name}
              onChange={handleChange}
              placeholder="Search by name..."
              className="search-input"
            />
          </div>

          <div className="search-field">
            <label htmlFor="category">Category</label>
            <input
              type="text"
              id="category"
              name="category"
              value={searchParams.category}
              onChange={handleChange}
              placeholder="Search by category..."
              className="search-input"
            />
          </div>
        </div>

        <div className="search-row">
          <div className="search-field">
            <label htmlFor="min_price">Min Price</label>
            <input
              type="number"
              id="min_price"
              name="min_price"
              value={searchParams.min_price}
              onChange={handleChange}
              placeholder="0.00"
              min="0"
              step="0.01"
              className="search-input"
            />
          </div>

          <div className="search-field">
            <label htmlFor="max_price">Max Price</label>
            <input
              type="number"
              id="max_price"
              name="max_price"
              value={searchParams.max_price}
              onChange={handleChange}
              placeholder="100.00"
              min="0"
              step="0.01"
              className="search-input"
            />
          </div>
        </div>

        <div className="search-buttons">
          <button type="submit" className="search-button">
            Search
          </button>
          <button type="button" onClick={handleClear} className="clear-button">
            Clear
          </button>
        </div>
      </form>
    </div>
  );
};

export default SearchBar;
