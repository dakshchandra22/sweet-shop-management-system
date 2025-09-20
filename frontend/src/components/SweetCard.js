import React from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useSweet } from '../contexts/SweetContext';
import { Card, Button, InputGroup, Form, Row, Col } from 'react-bootstrap';

const SweetCard = ({ sweet, onEdit }) => {
  const { user } = useAuth();
  const { purchaseSweet, deleteSweet, restockSweet } = useSweet();

  const handlePurchase = async (e) => {
    const qtyInput = e.target.closest('.purchase-section').querySelector('input[type="number"]');
    const quantity = qtyInput.value || 1;
    await purchaseSweet(sweet.id, quantity);
    qtyInput.value = '';
  };

  const handleRestock = async (e) => {
    const qtyInput = e.target.previousElementSibling;
    const quantity = qtyInput.value;
    if (quantity) {
      await restockSweet(sweet.id, quantity);
      qtyInput.value = '';
    }
  };

  const handleDelete = async () => {
    if (window.confirm(`Delete ${sweet.name}?`)) {
      await deleteSweet(sweet.id);
    }
  };

  return (
    <Card 
      className="h-100 shadow-sm" 
      style={{ 
        border: 'none',
        borderRadius: '15px',
        overflow: 'hidden',
        transition: 'transform 0.3s ease, box-shadow 0.3s ease'
      }}
      onMouseOver={(e) => {
        e.currentTarget.style.transform = 'translateY(-5px)';
        e.currentTarget.style.boxShadow = '0 8px 25px rgba(0,0,0,0.15)';
      }}
      onMouseOut={(e) => {
        e.currentTarget.style.transform = 'translateY(0)';
        e.currentTarget.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
      }}
    >
      {/* Pink Gradient Header */}
      <div 
        className="d-flex justify-content-center align-items-center py-4"
        style={{
          background: 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)',
          minHeight: '120px'
        }}
      >
        <span style={{ fontSize: '3rem' }}>🍭</span>
      </div>

      <Card.Body className="p-4">
        <Card.Title className="fw-bold mb-2" style={{ color: '#2c3e50', fontSize: '1.25rem' }}>
          {sweet.name}
        </Card.Title>
        <Card.Text className="text-muted mb-2" style={{ fontSize: '0.9rem' }}>
          {sweet.category}
        </Card.Text>
        <Card.Text className="fw-bold mb-3" style={{ color: '#3498db', fontSize: '1.1rem' }}>
          ${sweet.price}
        </Card.Text>

        {/* Purchase Section - Only for non-admin users */}
        {!user?.is_admin && (
          <div className="purchase-section mb-3">
            <InputGroup className="mb-2">
              <Form.Control
                type="number"
                min="1"
                max={sweet.quantity}
                placeholder="Qty"
                style={{ borderRadius: '8px 0 0 8px' }}
              />
              <Button
                onClick={handlePurchase}
                disabled={sweet.quantity === 0}
                style={{
                  background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
                  border: 'none',
                  borderRadius: '0 8px 8px 0',
                  fontWeight: '600'
                }}
              >
                Purchase
              </Button>
            </InputGroup>
            <small className="text-muted">Stock: {sweet.quantity}</small>
          </div>
        )}

        {/* Admin Stock Info */}
        {user?.is_admin && (
          <div className="admin-stock-info mb-3">
            <div className="text-center">
              <span className="badge bg-info fs-6 px-3 py-2" style={{ borderRadius: '10px' }}>
                Stock: {sweet.quantity}
              </span>
            </div>
          </div>
        )}

        {/* Admin Actions */}
        {user?.is_admin && (
          <div className="admin-actions">
            <Row className="g-2">
              <Col xs={6}>
                <Button
                  variant="outline-primary"
                  size="sm"
                  onClick={() => onEdit(sweet)}
                  className="w-100"
                  style={{ borderRadius: '8px' }}
                >
                  Edit
                </Button>
              </Col>
              <Col xs={6}>
                <Button
                  variant="outline-danger"
                  size="sm"
                  onClick={handleDelete}
                  className="w-100"
                  style={{ borderRadius: '8px' }}
                >
                  Delete
                </Button>
              </Col>
            </Row>
            <Row className="g-2 mt-2">
              <Col xs={8}>
                <Form.Control
                  type="number"
                  placeholder="Add stock"
                  size="sm"
                  style={{ borderRadius: '8px' }}
                />
              </Col>
              <Col xs={4}>
                <Button
                  variant="success"
                  size="sm"
                  onClick={handleRestock}
                  className="w-100"
                  style={{ borderRadius: '8px' }}
                >
                  Restock
                </Button>
              </Col>
            </Row>
          </div>
        )}
      </Card.Body>
    </Card>
  );
};

export default SweetCard;
