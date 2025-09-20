import React from 'react';
import { render, screen } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import App from '../App';

// Mock the contexts
jest.mock('../contexts/AuthContext', () => ({
  useAuth: () => ({
    user: null,
    login: jest.fn(),
    logout: jest.fn(),
    register: jest.fn()
  })
}));

jest.mock('../contexts/SweetContext', () => ({
  useSweet: () => ({
    sweets: [],
    loading: false,
    fetchSweets: jest.fn(),
    createSweet: jest.fn(),
    updateSweet: jest.fn(),
    deleteSweet: jest.fn(),
    purchaseSweet: jest.fn()
  })
}));

const renderWithRouter = (component) => {
  return render(
    <BrowserRouter>
      {component}
    </BrowserRouter>
  );
};

describe('App Component', () => {
  test('renders without crashing', () => {
    renderWithRouter(<App />);
    expect(screen.getByText(/Sweet Shop Management System/i)).toBeInTheDocument();
  });

  test('shows login form when user is not authenticated', () => {
    renderWithRouter(<App />);
    expect(screen.getByText(/Login/i)).toBeInTheDocument();
    expect(screen.getByText(/Register/i)).toBeInTheDocument();
  });
});
