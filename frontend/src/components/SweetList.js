import React from 'react';
import SweetCard from './SweetCard';
import { Container, Row, Col, Alert } from 'react-bootstrap';

const SweetList = ({ sweets, onEditSweet }) => {
  if (sweets.length === 0) {
    return (
      <Container className="text-center py-5">
        <Alert variant="info" className="border-0" style={{ borderRadius: '15px' }}>
          <h4 className="mb-3">No sweets found</h4>
          <p className="mb-0">Try adjusting your search or add some sweets!</p>
        </Alert>
      </Container>
    );
  }

  return (
    <Container>
      <Row className="g-4">
        {sweets.map(sweet => (
          <Col key={sweet.id} xs={12} sm={6} lg={4} xl={3}>
            <SweetCard
              sweet={sweet}
              onEdit={onEditSweet}
            />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default SweetList;
