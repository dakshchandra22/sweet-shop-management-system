import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';
import config from '../config';

const SweetContext = createContext();

export const useSweet = () => {
  const context = useContext(SweetContext);
  if (!context) {
    throw new Error('useSweet must be used within a SweetProvider');
  }
  return context;
};

export const SweetProvider = ({ children }) => {
  const [sweets, setSweets] = useState([]);
  const [loading, setLoading] = useState(false);

  // Simple API calls
  const fetchSweets = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${config.API_BASE_URL}/sweets`);
      setSweets(response.data);
    } catch (err) {
      console.error('Error fetching sweets:', err);
    } finally {
      setLoading(false);
    }
  };

  const createSweet = async (sweetData) => {
    try {
      const token = localStorage.getItem('token');
      await axios.post(`${config.API_BASE_URL}/sweets`, sweetData, {
        headers: { Authorization: `Bearer ${token}` }
      });
      await fetchSweets();
      return { success: true };
    } catch (err) {
      return { success: false, error: err.response?.data?.detail || 'Failed to create sweet' };
    }
  };

  const updateSweet = async (id, sweetData) => {
    try {
      const token = localStorage.getItem('token');
      await axios.put(`${config.API_BASE_URL}/sweets/${id}`, sweetData, {
        headers: { Authorization: `Bearer ${token}` }
      });
      await fetchSweets();
      return { success: true };
    } catch (err) {
      return { success: false, error: err.response?.data?.detail || 'Failed to update sweet' };
    }
  };

  const deleteSweet = async (id) => {
    try {
      const token = localStorage.getItem('token');
      await axios.delete(`${config.API_BASE_URL}/sweets/${id}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      await fetchSweets();
      return { success: true };
    } catch (err) {
      return { success: false, error: err.response?.data?.detail || 'Failed to delete sweet' };
    }
  };

  const purchaseSweet = async (id, quantity) => {
    try {
      const token = localStorage.getItem('token');
      await axios.post(`${config.API_BASE_URL}/sweets/${id}/purchase`, 
        { quantity: parseInt(quantity) }, 
        { headers: { Authorization: `Bearer ${token}` } }
      );
      await fetchSweets();
      return { success: true };
    } catch (err) {
      return { success: false, error: err.response?.data?.detail || 'Failed to purchase sweet' };
    }
  };

  const restockSweet = async (id, quantity) => {
    try {
      const token = localStorage.getItem('token');
      await axios.post(`${config.API_BASE_URL}/sweets/${id}/restock`, 
        { quantity: parseInt(quantity) }, 
        { headers: { Authorization: `Bearer ${token}` } }
      );
      await fetchSweets();
      return { success: true };
    } catch (err) {
      return { success: false, error: err.response?.data?.detail || 'Failed to restock sweet' };
    }
  };

  useEffect(() => {
    fetchSweets();
  }, []);

  const value = {
    sweets,
    loading,
    fetchSweets,
    createSweet,
    updateSweet,
    deleteSweet,
    purchaseSweet,
    restockSweet
  };

  return (
    <SweetContext.Provider value={value}>
      {children}
    </SweetContext.Provider>
  );
};
