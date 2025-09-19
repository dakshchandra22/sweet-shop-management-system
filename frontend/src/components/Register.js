import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { Card, Form, Button, Alert, Container, Row, Col } from 'react-bootstrap';

const Register = ({ onSuccess, onPageChange }) => {
  const [form, setForm] = useState({ email: '', username: '', password: '' });
  const [error, setError] = useState('');
  const [passwordStrength, setPasswordStrength] = useState('');
  const { register } = useAuth();

  const validatePassword = (password) => {
    const hasUpperCase = /[A-Z]/.test(password);
    const hasLowerCase = /[a-z]/.test(password);
    const hasNumbers = /\d/.test(password);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(password);
    const isLongEnough = password.length >= 8;

    if (!isLongEnough) return { valid: false, message: 'Password must be at least 8 characters long' };
    
    // Count criteria met
    const criteriaMet = [hasUpperCase, hasLowerCase, hasNumbers, hasSpecialChar].filter(Boolean).length;
    
    if (criteriaMet < 3) {
      return { valid: false, message: `Password must meet at least 3 criteria: uppercase, lowercase, number, special character (${criteriaMet}/4 met)` };
    }
    
    return { valid: true, message: 'Strong password!' };
  };

  const handlePasswordChange = (e) => {
    const password = e.target.value;
    setForm({...form, password});
    
    if (password.length > 0) {
      const validation = validatePassword(password);
      setPasswordStrength(validation.message);
    } else {
      setPasswordStrength('');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    const passwordValidation = validatePassword(form.password);
    if (!passwordValidation.valid) {
      setError(passwordValidation.message);
      return;
    }
    
    const result = await register(form);
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
              {/* Header with gradient */}
              <div 
                className="text-center py-4"
                style={{
                  background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
                  color: 'white'
                }}
              >
                <h2 className="mb-0 fw-bold">Register for Sweet Shop</h2>
                <p className="mb-0 opacity-75">Join us and discover amazing sweets!</p>
              </div>

              <Card.Body className="p-5">
                {error && (
                  <Alert variant="danger" className="mb-4" style={{ borderRadius: '10px' }}>
                    {error}
                  </Alert>
                )}
                
                <Form onSubmit={handleSubmit}>
                  <Form.Group className="mb-4">
                    <Form.Label className="fw-semibold">Email</Form.Label>
                    <Form.Control
                      type="email"
                      placeholder="Enter your email"
                      value={form.email}
                      onChange={(e) => setForm({...form, email: e.target.value})}
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
                    <Form.Label className="fw-semibold">Username</Form.Label>
                    <Form.Control
                      type="text"
                      placeholder="Choose a username"
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
                      placeholder="Create a strong password"
                      value={form.password}
                      onChange={handlePasswordChange}
                      required
                      style={{
                        borderRadius: '10px',
                        border: '2px solid #e9ecef',
                        padding: '12px 16px',
                        fontSize: '1rem'
                      }}
                    />
                            <div className="mt-2">
                              <small className="text-muted">
                                Password must be 8+ characters and meet at least 3 of: uppercase, lowercase, number, special character
                              </small>
                      {passwordStrength && (
                        <div className={`mt-1 ${passwordStrength === 'Strong password!' ? 'text-success' : 'text-danger'}`}>
                          <small>{passwordStrength}</small>
                        </div>
                      )}
                    </div>
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
                    Register
                  </Button>
                </Form>

                <div className="text-center mt-4">
                  <p className="text-muted mb-0">
                    Already have an account?{' '}
                    <button 
                      onClick={() => onPageChange('login')}
                      className="text-decoration-none fw-semibold border-0 bg-transparent"
                      style={{ color: '#9c27b0' }}
                    >
                      Login here
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

export default Register;
