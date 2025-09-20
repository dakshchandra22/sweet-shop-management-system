import React, { useState, useEffect } from 'react';
import { Card, Form, Button, Row, Col, Container } from 'react-bootstrap';
import { useAuth } from '../contexts/AuthContext';

const SearchBar = ({ searchTerm, onSearchChange, onAddNew, onSortChange }) => {
  const { user } = useAuth();
  const [filters, setFilters] = useState({
    name: '',
    sortBy: ''
  });

  const handleFilterChange = (field, value) => {
    setFilters(prev => ({ ...prev, [field]: value }));
  };

  // Real-time search effect - triggers search as you type
  useEffect(() => {
    onSearchChange(filters.name);
  }, [filters.name, onSearchChange]);

  const handleSearch = () => {
    // Apply search filter
    onSearchChange(filters.name);
  };

  const handleSort = (sortType) => {
    setFilters(prev => ({ ...prev, sortBy: sortType }));
    onSortChange(sortType);
  };

  const handleClear = () => {
    setFilters({
      name: '',
      sortBy: ''
    });
    onSearchChange('');
    onSortChange('');
  };

  return (
    <Container className="mb-4">
      {/* Welcome Section */}
      <div className="text-center mb-4">
        <h1 className="fw-bold mb-2" style={{ color: '#2c3e50', fontSize: '2.5rem' }}>
          Welcome to Sweet Shop
        </h1>
        <p className="text-muted fs-5">Discover our delicious collection of sweets.</p>
        
        {/* Admin New Sweet Button - Below Welcome */}
        {user?.is_admin && (
          <div className="mt-3">
            <Button
              onClick={onAddNew}
              style={{
                background: 'linear-gradient(135deg, #28a745 0%, #20c997 100%)',
                border: 'none',
                borderRadius: '10px',
                padding: '12px 24px',
                fontWeight: '600',
                boxShadow: '0 4px 15px rgba(40, 167, 69, 0.3)',
                transition: 'all 0.3s ease'
              }}
              onMouseOver={(e) => {
                e.target.style.transform = 'translateY(-2px)';
                e.target.style.boxShadow = '0 6px 20px rgba(40, 167, 69, 0.4)';
              }}
              onMouseOut={(e) => {
                e.target.style.transform = 'translateY(0)';
                e.target.style.boxShadow = '0 4px 15px rgba(40, 167, 69, 0.3)';
              }}
            >
              ➕ Add New Sweet
            </Button>
          </div>
        )}
      </div>

      {/* Search and Filter Card */}
      <Card className="shadow-sm border-0" style={{ borderRadius: '15px' }}>
        <Card.Body className="p-4">
          <Row className="g-3">
            <Col md={6}>
              <Form.Group>
                <Form.Label className="fw-semibold">Search</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Search sweets as you type..."
                  value={filters.name}
                  onChange={(e) => handleFilterChange('name', e.target.value)}
                  style={{
                    borderRadius: '10px',
                    border: '2px solid #e9ecef',
                    padding: '12px 16px'
                  }}
                />
                <Form.Text className="text-muted">
                  Results filter automatically as you type, or use the Search button
                </Form.Text>
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group>
                <Form.Label className="fw-semibold">Sort by Price</Form.Label>
                <div className="d-flex gap-2">
                  <Button
                    variant={filters.sortBy === 'low-high' ? 'primary' : 'outline-primary'}
                    onClick={() => handleSort('low-high')}
                    style={{
                      borderRadius: '10px',
                      padding: '12px 16px',
                      fontWeight: '600',
                      flex: 1
                    }}
                  >
                    Low to High
                  </Button>
                  <Button
                    variant={filters.sortBy === 'high-low' ? 'primary' : 'outline-primary'}
                    onClick={() => handleSort('high-low')}
                    style={{
                      borderRadius: '10px',
                      padding: '12px 16px',
                      fontWeight: '600',
                      flex: 1
                    }}
                  >
                    High to Low
                  </Button>
                </div>
              </Form.Group>
            </Col>
          </Row>
          
          <div className="d-flex gap-3 mt-3 justify-content-center">
            <Button
              onClick={handleSearch}
              style={{
                background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
                border: 'none',
                borderRadius: '10px',
                padding: '12px 24px',
                fontWeight: '600'
              }}
            >
              🔍 Search
            </Button>
            <Button
              variant="secondary"
              onClick={handleClear}
              style={{
                borderRadius: '10px',
                padding: '12px 24px',
                fontWeight: '600'
              }}
            >
              Clear All Filters
            </Button>
          </div>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default SearchBar;
