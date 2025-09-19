import React from 'react';
import { useAuth } from '../contexts/AuthContext';
import { Navbar, Nav, Container, Badge } from 'react-bootstrap';

const Header = ({ onPageChange, onLogout }) => {
  const { user, logout } = useAuth();

  return (
    <Navbar 
      expand="lg" 
      className="mb-4" 
      style={{
        background: 'linear-gradient(135deg, #9c27b0 0%, #673ab7 100%)',
        boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
      }}
    >
      <Container>
        <Navbar.Brand href="#home" className="fw-bold text-white d-flex align-items-center">
          <span style={{ fontSize: '1.5rem', marginRight: '10px' }}>🍭</span>
          Sweet Shop
        </Navbar.Brand>
        
        <Navbar.Toggle aria-controls="basic-navbar-nav" className="border-0" />
        
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="ms-auto d-flex align-items-center">
            {user ? (
              <>
                <Navbar.Text className="me-3 text-white">
                  Hello {user.username}
                  {user.is_admin && (
                    <Badge bg="warning" className="ms-2">Admin</Badge>
                  )}
                </Navbar.Text>
                <button 
                  onClick={onLogout || logout} 
                  className="btn text-white fw-semibold px-3 py-2"
                  style={{
                    background: 'rgba(255,255,255,0.2)',
                    border: '1px solid rgba(255,255,255,0.3)',
                    borderRadius: '8px',
                    transition: 'all 0.3s ease'
                  }}
                  onMouseOver={(e) => {
                    e.target.style.background = 'rgba(255,255,255,0.3)';
                  }}
                  onMouseOut={(e) => {
                    e.target.style.background = 'rgba(255,255,255,0.2)';
                  }}
                >
                  Logout
                </button>
              </>
            ) : (
              <Navbar.Text className="text-white">Welcome! Please sign in to shop.</Navbar.Text>
            )}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Header;
