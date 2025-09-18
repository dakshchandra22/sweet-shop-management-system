import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Configure axios defaults
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    }
  }, []);

  const login = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:8000/api/auth/login', {
        username,
        password
      });

      const { access_token } = response.data;
      localStorage.setItem('token', access_token);
      localStorage.setItem('username', username);
      axios.defaults.headers.common['Authorization'] = `Bearer ${access_token}`;

      // Get user info from token (simplified - in real app, decode JWT or fetch user)
      // For now, we'll check if username is 'admin' to determine admin status
      setUser({ username, is_admin: username === 'admin' });
      return { success: true };
    } catch (error) {
      let errorMessage = 'Login failed';
      if (error.response?.data) {
        if (typeof error.response.data === 'string') {
          errorMessage = error.response.data;
        } else if (error.response.data.detail) {
          errorMessage = error.response.data.detail;
        } else if (Array.isArray(error.response.data)) {
          errorMessage = error.response.data.map(err => err.msg || err).join(', ');
        }
      }
      return { 
        success: false, 
        error: errorMessage
      };
    }
  };

  const register = async (userData) => {
    try {
      const response = await axios.post('http://localhost:8000/api/auth/register', userData);
      return { success: true, data: response.data };
    } catch (error) {
      let errorMessage = 'Registration failed';
      if (error.response?.data) {
        if (typeof error.response.data === 'string') {
          errorMessage = error.response.data;
        } else if (error.response.data.detail) {
          errorMessage = error.response.data.detail;
        } else if (Array.isArray(error.response.data)) {
          errorMessage = error.response.data.map(err => err.msg || err).join(', ');
        }
      }
      return { 
        success: false, 
        error: errorMessage
      };
    }
  };

  const logout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    delete axios.defaults.headers.common['Authorization'];
    setUser(null);
  };

  const checkAuth = async () => {
    const token = localStorage.getItem('token');
    if (token) {
      try {
        // In a real app, you'd verify the token with the backend
        // For simplicity, we'll check if we have a stored username
        const storedUsername = localStorage.getItem('username');
        if (storedUsername) {
          setUser({ username: storedUsername, is_admin: storedUsername === 'admin' });
        } else {
          setUser({ username: 'user', is_admin: false });
        }
      } catch (error) {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        delete axios.defaults.headers.common['Authorization'];
      }
    }
    setLoading(false);
  };

  useEffect(() => {
    checkAuth();
  }, []);

  const value = {
    user,
    login,
    register,
    logout,
    loading
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
