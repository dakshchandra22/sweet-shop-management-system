import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

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
  const [error, setError] = useState(null);

  const fetchSweets = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get('http://localhost:8000/api/sweets/');
      setSweets(response.data);
    } catch (err) {
      setError('Failed to fetch sweets');
      console.error('Error fetching sweets:', err);
    } finally {
      setLoading(false);
    }
  };

  const searchSweets = async (searchParams) => {
    setLoading(true);
    setError(null);
    try {
      const params = new URLSearchParams();
      if (searchParams.name) params.append('name', searchParams.name);
      if (searchParams.category) params.append('category', searchParams.category);
      if (searchParams.min_price) params.append('price_min', searchParams.min_price);
      if (searchParams.max_price) params.append('price_max', searchParams.max_price);

      const response = await axios.get(`http://localhost:8000/api/sweets/search?${params}`);
      setSweets(response.data);
    } catch (err) {
      setError('Failed to search sweets');
      console.error('Error searching sweets:', err);
    } finally {
      setLoading(false);
    }
  };

  const createSweet = async (sweetData) => {
    try {
      const response = await axios.post('http://localhost:8000/api/sweets/', sweetData);
      setSweets(prev => [...prev, response.data]);
      return { success: true, data: response.data };
    } catch (err) {
      return { 
        success: false, 
        error: err.response?.data?.detail || 'Failed to create sweet' 
      };
    }
  };

  const updateSweet = async (id, sweetData) => {
    try {
      const response = await axios.put(`http://localhost:8000/api/sweets/${id}`, sweetData);
      setSweets(prev => prev.map(sweet => 
        sweet.id === id ? response.data : sweet
      ));
      return { success: true, data: response.data };
    } catch (err) {
      return { 
        success: false, 
        error: err.response?.data?.detail || 'Failed to update sweet' 
      };
    }
  };

  const deleteSweet = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/sweets/${id}`);
      setSweets(prev => prev.filter(sweet => sweet.id !== id));
      return { success: true };
    } catch (err) {
      return { 
        success: false, 
        error: err.response?.data?.detail || 'Failed to delete sweet' 
      };
    }
  };

  const purchaseSweet = async (id, quantity) => {
    try {
      const requestData = { quantity: parseInt(quantity) };
      
      const response = await axios.post(`http://localhost:8000/api/sweets/${id}/purchase`, requestData);
      
      // Refresh sweets to get updated quantities
      await fetchSweets();
      return { success: true, data: response.data };
    } catch (err) {
      return { 
        success: false, 
        error: err.response?.data?.detail || 'Failed to purchase sweet' 
      };
    }
  };

  const restockSweet = async (id, quantity) => {
    try {
      const response = await axios.post(`http://localhost:8000/api/sweets/${id}/restock`, {
        quantity
      });
      // Refresh sweets to get updated quantities
      await fetchSweets();
      return { success: true, data: response.data };
    } catch (err) {
      return { 
        success: false, 
        error: err.response?.data?.detail || 'Failed to restock sweet' 
      };
    }
  };

  useEffect(() => {
    fetchSweets();
  }, []);

  const value = {
    sweets,
    loading,
    error,
    fetchSweets,
    searchSweets,
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
