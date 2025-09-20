import React from 'react';
import { Card, Button, Badge } from 'react-bootstrap';
import { useAuth } from '../contexts/AuthContext';
import { useSweet } from '../contexts/SweetContext';

const SweetCard = ({ sweet, onEdit }) => {
  const { user } = useAuth();
  const { purchaseSweet, restockSweet } = useSweet();
  const [quantity, setQuantity] = React.useState(1);

  const handlePurchase = async () => {
    if (quantity > 0 && quantity <= sweet.stock) {
      const result = await purchaseSweet(sweet.id, quantity);
      if (result.success) {
        alert(`Successfully purchased ${quantity} ${sweet.name}(s)!`);
        setQuantity(1);
      } else {
        alert(result.error);
      }
    } else {
      alert('Invalid quantity or insufficient stock!');
    }
  };

  const handleRestock = async () => {
    const restockQty = prompt('Enter restock quantity:');
    if (restockQty && restockQty > 0) {
      const result = await restockSweet(sweet.id, restockQty);
      if (result.success) {
        alert(`Successfully restocked ${restockQty} ${sweet.name}(s)!`);
      } else {
        alert(result.error);
      }
    }
  };

  return (
    <Card className="h-100 shadow-sm" style={{ borderRadius: '15px', border: 'none' }}>
      <Card.Img 
        variant="top" 
        src={sweet.image_url || '/api/placeholder/300/200'} 
        style={{ height: '200px', objectFit: 'cover', borderRadius: '15px 15px 0 0' }}
        onError={(e) => {
          e.target.src = 'data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAwIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cmVjdCB3aWR0aD0iMTAwJSIgaGVpZ2h0PSIxMDAlIiBmaWxsPSIjZGRkIi8+PHRleHQgeD0iNTAlIiB5PSI1MCUiIGZvbnQtZmFtaWx5PSJBcmlhbCIgZm9udC1zaXplPSIxNCIgZmlsbD0iIzk5OSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zZW0iPk5vIEltYWdlPC90ZXh0Pjwvc3ZnPg==';
        }}
      />
      <Card.Body className="d-flex flex-column">
        <div className="mb-2">
          <Badge bg="secondary" className="mb-2">{sweet.category}</Badge>
          <Card.Title className="h5 mb-2">{sweet.name}</Card.Title>
          <Card.Text className="text-muted small mb-2">
            {sweet.description || 'Delicious sweet treat!'}
          </Card.Text>
        </div>
        
        <div className="mt-auto">
          <div className="d-flex justify-content-between align-items-center mb-3">
            <span className="h5 text-primary mb-0">${sweet.price}</span>
            <Badge 
              bg={sweet.stock > 10 ? 'success' : sweet.stock > 0 ? 'warning' : 'danger'}
              className="px-2 py-1"
            >
              {sweet.stock} in stock
            </Badge>
          </div>

          {user ? (
            <div>
              {user.is_admin ? (
                <div className="d-grid gap-2">
                  <Button 
                    variant="outline-primary" 
                    size="sm" 
                    onClick={() => onEdit(sweet)}
                  >
                    Edit
                  </Button>
                  <Button 
                    variant="outline-success" 
                    size="sm" 
                    onClick={handleRestock}
                  >
                    Restock
                  </Button>
                </div>
              ) : (
                <div className="d-grid gap-2">
                  <div className="d-flex gap-2 mb-2">
                    <input
                      type="number"
                      min="1"
                      max={sweet.stock}
                      value={quantity}
                      onChange={(e) => setQuantity(parseInt(e.target.value) || 1)}
                      className="form-control form-control-sm"
                      style={{ width: '60px' }}
                    />
                    <Button 
                      variant="primary" 
                      size="sm" 
                      onClick={handlePurchase}
                      disabled={sweet.stock === 0}
                      className="flex-grow-1"
                    >
                      {sweet.stock === 0 ? 'Out of Stock' : 'Buy'}
                    </Button>
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="text-center">
              <small className="text-muted">Please login to purchase</small>
            </div>
          )}
        </div>
      </Card.Body>
    </Card>
  );
};

export default SweetCard;
