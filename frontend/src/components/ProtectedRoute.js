import React from 'react';
import { Navigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

const ProtectedRoute = ({ children, adminOnly = false }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="loading-container">
        <div className="loading">Loading...</div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" replace />;
  }

  if (adminOnly && !user.is_admin) {
    return (
      <div className="error-container">
        <h2>Access Denied</h2>
        <p>You need admin privileges to access this page.</p>
      </div>
    );
  }

  return children;
};

export default ProtectedRoute;
