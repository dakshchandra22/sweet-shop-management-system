import React, { useState, useEffect } from 'react';
import { useSweet } from '../contexts/SweetContext';
import { Modal, Form, Button, Row, Col } from 'react-bootstrap';

const SweetForm = ({ editingSweet, onCancel, show }) => {
  const [form, setForm] = useState({ name: '', category: '', price: '', quantity: '' });
  const { createSweet, updateSweet } = useSweet();

  useEffect(() => {
    if (editingSweet) {
      setForm({
        name: editingSweet.name || '',
        category: editingSweet.category || '',
        price: editingSweet.price ? editingSweet.price.toString() : '',
        quantity: editingSweet.quantity ? editingSweet.quantity.toString() : ''
      });
    } else {
      setForm({ name: '', category: '', price: '', quantity: '' });
    }
  }, [editingSweet]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const sweetData = {
      name: form.name,
      category: form.category,
      price: parseFloat(form.price),
      quantity: parseInt(form.quantity)
    };

    if (editingSweet && editingSweet.id) {
      await updateSweet(editingSweet.id, sweetData);
    } else {
      await createSweet(sweetData);
    }
    
    onCancel();
  };

  return (
    <Modal 
      show={show} 
      onHide={onCancel} 
      size="lg" 
      centered
      backdrop="static"
    >
      <Modal.Header 
        closeButton 
        style={{
          background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
          color: 'white',
          border: 'none'
        }}
      >
        <Modal.Title className="fw-bold">
          {editingSweet && editingSweet.id ? 'Edit Sweet' : 'Add New Sweet'}
        </Modal.Title>
      </Modal.Header>
      
      <Modal.Body className="p-4">
        <Form onSubmit={handleSubmit}>
          <Row className="g-3">
            <Col md={6}>
              <Form.Group>
                <Form.Label className="fw-semibold">Name</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter sweet name"
                  value={form.name}
                  onChange={(e) => setForm({...form, name: e.target.value})}
                  required
                  style={{
                    borderRadius: '10px',
                    border: '2px solid #e9ecef',
                    padding: '12px 16px'
                  }}
                />
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group>
                <Form.Label className="fw-semibold">Category</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Enter category"
                  value={form.category}
                  onChange={(e) => setForm({...form, category: e.target.value})}
                  required
                  style={{
                    borderRadius: '10px',
                    border: '2px solid #e9ecef',
                    padding: '12px 16px'
                  }}
                />
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group>
                <Form.Label className="fw-semibold">Price</Form.Label>
                <Form.Control
                  type="number"
                  step="0.01"
                  placeholder="0.00"
                  value={form.price}
                  onChange={(e) => setForm({...form, price: e.target.value})}
                  required
                  style={{
                    borderRadius: '10px',
                    border: '2px solid #e9ecef',
                    padding: '12px 16px'
                  }}
                />
              </Form.Group>
            </Col>
            <Col md={6}>
              <Form.Group>
                <Form.Label className="fw-semibold">Quantity</Form.Label>
                <Form.Control
                  type="number"
                  placeholder="0"
                  value={form.quantity}
                  onChange={(e) => setForm({...form, quantity: e.target.value})}
                  required
                  style={{
                    borderRadius: '10px',
                    border: '2px solid #e9ecef',
                    padding: '12px 16px'
                  }}
                />
              </Form.Group>
            </Col>
          </Row>
        </Form>
      </Modal.Body>
      
      <Modal.Footer className="border-0 p-4">
        <Button
          variant="secondary"
          onClick={onCancel}
          style={{
            borderRadius: '10px',
            padding: '12px 24px',
            fontWeight: '600'
          }}
        >
          Cancel
        </Button>
        <Button
          onClick={handleSubmit}
          style={{
            background: 'linear-gradient(135deg, #28a745 0%, #20c997 100%)',
            border: 'none',
            borderRadius: '10px',
            padding: '12px 24px',
            fontWeight: '600'
          }}
        >
          {editingSweet && editingSweet.id ? 'Update' : 'Add'} Sweet
        </Button>
      </Modal.Footer>
    </Modal>
  );
};

export default SweetForm;
