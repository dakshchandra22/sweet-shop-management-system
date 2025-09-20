import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import SearchBar from '../../components/SearchBar';

// Mock the AuthContext
const mockUseAuth = {
  user: { username: 'testuser', is_admin: false }
};

jest.mock('../../contexts/AuthContext', () => ({
  useAuth: () => mockUseAuth
}));

describe('SearchBar Component', () => {
  const mockProps = {
    searchTerm: '',
    onSearchChange: jest.fn(),
    onAddNew: jest.fn(),
    onSortChange: jest.fn()
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders search input field', () => {
    render(<SearchBar {...mockProps} />);
    
    expect(screen.getByPlaceholderText(/Search sweets as you type/i)).toBeInTheDocument();
    expect(screen.getByText(/Search/i)).toBeInTheDocument();
  });

  test('renders sort buttons', () => {
    render(<SearchBar {...mockProps} />);
    
    expect(screen.getByText(/Low to High/i)).toBeInTheDocument();
    expect(screen.getByText(/High to Low/i)).toBeInTheDocument();
  });

  test('calls onSearchChange when typing in search input', async () => {
    render(<SearchBar {...mockProps} />);
    
    const searchInput = screen.getByPlaceholderText(/Search sweets as you type/i);
    fireEvent.change(searchInput, { target: { value: 'gulab jamun' } });
    
    await waitFor(() => {
      expect(mockProps.onSearchChange).toHaveBeenCalledWith('gulab jamun');
    });
  });

  test('calls onSortChange when clicking sort buttons', () => {
    render(<SearchBar {...mockProps} />);
    
    const lowToHighButton = screen.getByText(/Low to High/i);
    fireEvent.click(lowToHighButton);
    
    expect(mockProps.onSortChange).toHaveBeenCalledWith('low-high');
  });

  test('calls onSortChange when clicking high to low button', () => {
    render(<SearchBar {...mockProps} />);
    
    const highToLowButton = screen.getByText(/High to Low/i);
    fireEvent.click(highToLowButton);
    
    expect(mockProps.onSortChange).toHaveBeenCalledWith('high-low');
  });

  test('calls onAddNew when clicking add new button (admin only)', () => {
    mockUseAuth.user.is_admin = true;
    render(<SearchBar {...mockProps} />);
    
    const addNewButton = screen.getByText(/Add New Sweet/i);
    fireEvent.click(addNewButton);
    
    expect(mockProps.onAddNew).toHaveBeenCalled();
  });

  test('does not show add new button for non-admin users', () => {
    mockUseAuth.user.is_admin = false;
    render(<SearchBar {...mockProps} />);
    
    expect(screen.queryByText(/Add New Sweet/i)).not.toBeInTheDocument();
  });

  test('calls onSearchChange and onSortChange when clicking clear button', () => {
    render(<SearchBar {...mockProps} />);
    
    const clearButton = screen.getByText(/Clear All Filters/i);
    fireEvent.click(clearButton);
    
    expect(mockProps.onSearchChange).toHaveBeenCalledWith('');
    expect(mockProps.onSortChange).toHaveBeenCalledWith('');
  });

  test('shows helper text for search input', () => {
    render(<SearchBar {...mockProps} />);
    
    expect(screen.getByText(/Results filter automatically as you type/i)).toBeInTheDocument();
  });
});
