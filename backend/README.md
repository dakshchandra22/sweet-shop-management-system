# 🚀 Sweet Shop Management System - Backend

FastAPI-based RESTful API for the Sweet Shop Management System with MongoDB integration, JWT authentication, and comprehensive CRUD operations.

## 🛠️ Tech Stack

- **Framework**: FastAPI (Python 3.11+)
- **Database**: MongoDB
- **Authentication**: JWT tokens with bcrypt password hashing
- **Validation**: Pydantic v2
- **Testing**: pytest + pytest-asyncio
- **Server**: Uvicorn ASGI server

## 📁 Project Structure

```
backend/
├── routers/              # API route handlers
│   ├── auth.py          # Authentication endpoints
│   ├── sweets.py        # Sweet management endpoints
│   └── inventory.py     # Inventory management endpoints
├── tests/               # Test suite
│   ├── test_auth.py     # Authentication tests
│   ├── test_sweets.py   # Sweet management tests
│   └── test_inventory.py # Inventory tests
├── models.py            # Pydantic data models
├── auth.py              # Authentication utilities
├── database.py          # MongoDB connection
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── run_server.py        # Server startup script
└── run_tests.py         # Test runner script
```

## 🚀 Quick Start

### **1. Setup Environment**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **2. Start MongoDB**
Make sure MongoDB is running on your system.

### **3. Run Server**
```bash
# Option 1: Using startup script
python run_server.py

# Option 2: Direct uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### **4. Access API**
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📚 API Endpoints

### **Authentication**
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### **Sweet Management**
- `GET /api/sweets/` - Get all sweets (public)
- `GET /api/sweets/search` - Search sweets (public)
- `POST /api/sweets/` - Create sweet (admin only)
- `GET /api/sweets/{id}` - Get specific sweet
- `PUT /api/sweets/{id}` - Update sweet (admin only)
- `DELETE /api/sweets/{id}` - Delete sweet (admin only)

### **Inventory Management**
- `POST /api/sweets/{id}/purchase` - Purchase sweet
- `POST /api/sweets/{id}/restock` - Restock sweet (admin only)

## 🔐 Authentication

### **JWT Token System**
- Tokens expire in 30 minutes
- Bearer token authentication
- Role-based access control (admin/customer)

### **Default Admin Account**
- **Username**: `admin`
- **Password**: `admin123`

## 🧪 Testing

### **Run Tests**
```bash
# Run all tests
python run_tests.py

# Run specific test file
pytest tests/test_auth.py -v

# Run with coverage
pytest --cov=. tests/
```

### **Test Coverage**
- Authentication flow testing
- API endpoint validation
- Database integration testing
- Error handling scenarios
- Role-based access control

## 📊 Data Models

### **User Model**
```python
class User(BaseModel):
    id: str
    email: str
    username: str
    is_admin: bool
    created_at: datetime
```

### **Sweet Model**
```python
class Sweet(BaseModel):
    id: str
    name: str
    category: str
    price: float
    quantity: int
    created_at: datetime
    updated_at: datetime
```

### **Request Models**
- `UserCreate` - User registration
- `LoginRequest` - User login
- `SweetCreate` - Create sweet
- `SweetUpdate` - Update sweet
- `PurchaseRequest` - Purchase sweet
- `RestockRequest` - Restock sweet

## 🔧 Configuration

### **Environment Variables**
```bash
MONGODB_URI=mongodb://localhost:27017/sweetshop
SECRET_KEY=your-secret-key
DEBUG=true
```

### **Database Configuration**
- **Database**: `sweetshop`
- **Collections**: `users`, `sweets`
- **Connection**: MongoDB local instance

## 🚀 Production Deployment

### **Requirements**
- Python 3.11+
- MongoDB (local or Atlas)
- Uvicorn ASGI server
- Environment variables configured

### **Docker Support**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 📈 Performance

### **Optimizations**
- Connection pooling for MongoDB
- Async/await for I/O operations
- Pydantic validation for data integrity
- JWT token caching
- CORS middleware for frontend integration

### **Monitoring**
- Health check endpoint
- Request logging
- Error tracking
- Performance metrics

## 🔒 Security Features

- **Password Hashing**: bcrypt with salt
- **JWT Tokens**: Secure token-based authentication
- **CORS**: Configured for frontend communication
- **Input Validation**: Pydantic model validation
- **Role-Based Access**: Admin/customer permissions
- **Error Handling**: Secure error responses

## 🐛 Troubleshooting

### **Common Issues**
1. **MongoDB Connection**: Ensure MongoDB is running
2. **Port Conflicts**: Check if port 8000 is available
3. **Dependencies**: Run `pip install -r requirements.txt`
4. **Environment**: Activate virtual environment

### **Debug Mode**
```bash
# Enable debug logging
export DEBUG=true
uvicorn main:app --reload --log-level debug
```

## 📝 Development

### **Code Style**
- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes
- Write comprehensive tests

### **Adding New Endpoints**
1. Create route in appropriate router file
2. Add Pydantic models if needed
3. Write tests for new endpoint
4. Update API documentation

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Ensure all tests pass
5. Submit pull request

---

**Backend API Version**: 1.0.0  
**Last Updated**: September 18, 2025  
**Status**: Production Ready
