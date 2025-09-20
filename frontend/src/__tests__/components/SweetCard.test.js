import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import SweetCard from '../../components/SweetCard';

// Mock the AuthContext
const mockUseAuth = {
  user: { username: 'testuser', is_admin: false }
};

jest.mock('../../contexts/AuthContext', () => ({
  useAuth: () => mockUseAuth
}));

// Mock the SweetContext
const mockUseSweet = {
  purchaseSweet: jest.fn()
};

jest.mock('../../contexts/SweetContext', () => ({
  useSweet: () => mockUseSweet
}));

describe('SweetCard Component', () => {
  const mockSweet = {
    id: '1',
    name: 'Gulab Jamun',
    description: 'Soft, spongy milk dumplings soaked in rose-flavored syrup',
    category: 'Traditional',
    price: 25.0,
    quantity: 50,
    image_url: 'https://example.com/gulab-jamun.jpg'
  };

  const mockProps = {
    sweet: mockSweet,
    onEditSweet: jest.fn()
  };

  beforeEach(() => {
    jest.clearAllMocks();
  });

  test('renders sweet information correctly', () => {
    render(<SweetCard {...mockProps} />);
    
    expect(screen.getByText('Gulab Jamun')).toBeInTheDocument();
    expect(screen.getByText('Soft, spongy milk dumplings soaked in rose-flavored syrup')).toBeInTheDocument();
    expect(screen.getByText('Traditional')).toBeInTheDocument();
    expect(screen.getByText('₹25.0')).toBeInTheDocument();
    expect(screen.getByText('50 available')).toBeInTheDocument();
  });

  test('renders sweet image', () => {
    render(<SweetCard {...mockProps} />);
    
    const image = screen.getByAltText('Gulab Jamun');
    expect(image).toBeInTheDocument();
    expect(image).toHaveAttribute('src', 'https://example.com/gulab-jamun.jpg');
  });

  test('shows purchase button for customers', () => {
    mockUseAuth.user.is_admin = false;
    render(<SweetCard {...mockProps} />);
    
    expect(screen.getByText(/Purchase/i)).toBeInTheDocument();
  });

  test('shows edit button for admin users', () => {
    mockUseAuth.user.is_admin = true;
    render(<SweetCard {...mockProps} />);
    
    expect(screen.getByText(/Edit/i)).toBeInTheDocument();
  });

  test('calls onEditSweet when edit button is clicked', () => {
    mockUseAuth.user.is_admin = true;
    render(<SweetCard {...mockProps} />);
    
    const editButton = screen.getByText(/Edit/i);
    fireEvent.click(editButton);
    
    expect(mockProps.onEditSweet).toHaveBeenCalledWith(mockSweet);
  });

  test('handles purchase with valid quantity', async () => {
    mockUseAuth.user.is_admin = false;
    mockUseSweet.purchaseSweet.mockResolvedValueOnce({ success: true });
    
    render(<SweetCard {...mockProps} />);
    
    const quantityInput = screen.getByDisplayValue('1');
    const purchaseButton = screen.getByText(/Purchase/i);
    
    fireEvent.change(quantityInput, { target: { value: '2' } });
    fireEvent.click(purchaseButton);
    
    expect(mockUseSweet.purchaseSweet).toHaveBeenCalledWith('1', 2);
  });

  test('shows error for invalid quantity', async () => {
    mockUseAuth.user.is_admin = false;
    render(<SweetCard {...mockProps} />);
    
    const quantityInput = screen.getByDisplayValue('1');
    const purchaseButton = screen.getByText(/Purchase/i);
    
    fireEvent.change(quantityInput, { target: { value: '0' } });
    fireEvent.click(purchaseButton);
    
    expect(screen.getByText(/Please enter a valid quantity/i)).toBeInTheDocument();
    expect(mockUseSweet.purchaseSweet).not.toHaveBeenCalled();
  });

  test('shows error for quantity exceeding available stock', async () => {
    mockUseAuth.user.is_admin = false;
    render(<SweetCard {...mockProps} />);
    
    const quantityInput = screen.getByDisplayValue('1');
    const purchaseButton = screen.getByText(/Purchase/i);
    
    fireEvent.change(quantityInput, { target: { value: '100' } });
    fireEvent.click(purchaseButton);
    
    expect(screen.getByText(/Quantity exceeds available stock/i)).toBeInTheDocument();
    expect(mockUseSweet.purchaseSweet).not.toHaveBeenCalled();
  });

  test('shows out of stock message when quantity is 0', () => {
    const outOfStockSweet = { ...mockSweet, quantity: 0 };
    render(<SweetCard {...mockProps} sweet={outOfStockSweet} />);
    
    expect(screen.getByText(/Out of Stock/i)).toBeInTheDocument();
    expect(screen.queryByText(/Purchase/i)).not.toBeInTheDocument();
  });

  test('disables purchase button when out of stock', () => {
    const outOfStockSweet = { ...mockSweet, quantity: 0 };
    render(<SweetCard {...mockProps} sweet={outOfStockSweet} />);
    
    const purchaseButton = screen.queryByText(/Purchase/i);
    expect(purchaseButton).not.toBeInTheDocument();
  });
});
