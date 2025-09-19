import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { Card, Form, Button, Alert, Container, Row, Col } from 'react-bootstrap';

const Login = ({ onSuccess, onPageChange }) => {
  const [form, setForm] = useState({ username: '', password: '' });
  const [error, setError] = useState('');
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    const result = await login(form.username, form.password);
    if (result.success) {
      onSuccess();
    } else {
      setError(result.error);
    }
  };

  return (
    <div 
      className="min-vh-100 d-flex align-items-center"
      style={{
        background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        padding: '20px 0'
      }}
    >
      <Container>
        <Row className="justify-content-center">
          <Col xs={12} sm={10} md={8} lg={6} xl={5}>
            <Card 
              className="shadow-lg border-0"
              style={{ borderRadius: '20px', overflow: 'hidden' }}
            >
              <div 
                className="text-center py-4"
                style={{
                  background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
                  color: 'white'
                }}
              >
                <h2 className="mb-0 fw-bold">Login to Sweet Shop</h2>
                <p className="mb-0 opacity-75">Welcome back! Please sign in to continue.</p>
              </div>

              <Card.Body className="p-5">
                {error && (
                  <Alert variant="danger" className="mb-4" style={{ borderRadius: '10px' }}>
                    {error}
                  </Alert>
                )}
                
                <Form onSubmit={handleSubmit}>
                  <Form.Group className="mb-4">
                    <Form.Label className="fw-semibold">Username</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="Enter your username"
                      value={form.username}
                      onChange={(e) => setForm({...form, username: e.target.value})}
                      required
                      style={{
                        borderRadius: '10px',
                        border: '2px solid #e9ecef',
                        padding: '12px 16px',
                        fontSize: '1rem'
                      }}
                    />
                  </Form.Group>
                  
                  <Form.Group className="mb-4">
                    <Form.Label className="fw-semibold">Password</Form.Label>
                    <Form.Control
                      type="password"
                      placeholder="Enter your password"
                      value={form.password}
                      onChange={(e) => setForm({...form, password: e.target.value})}
                      required
                      style={{
                        borderRadius: '10px',
                        border: '2px solid #e9ecef',
                        padding: '12px 16px',
                        fontSize: '1rem'
                      }}
                    />
                  </Form.Group>
                  
                  <Button 
                    type="submit" 
                    className="w-100 py-3 fw-bold"
                    style={{
                      background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
                      border: 'none',
                      borderRadius: '10px',
                      fontSize: '1.1rem',
                      transition: 'all 0.3s ease'
                    }}
                    onMouseOver={(e) => {
                      e.target.style.transform = 'translateY(-2px)';
                      e.target.style.boxShadow = '0 8px 25px rgba(156, 39, 176, 0.3)';
                    }}
                    onMouseOut={(e) => {
                      e.target.style.transform = 'translateY(0)';
                      e.target.style.boxShadow = 'none';
                    }}
                  >
                    Login
                  </Button>
                </Form>

                <div className="text-center mt-4">
                  <p className="text-muted mb-0">
                    Don't have an account?{' '}
                    <button 
                      onClick={() => onPageChange('register')}
                      className="text-decoration-none fw-semibold border-0 bg-transparent"
                      style={{ color: '#9c27b0' }}
                    >
                      Register here
                    </button>
                  </p>
                </div>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Login;
