# 🍭 Sweet Shop Management System

A full-stack web application built with **Test-Driven Development (TDD)** methodology for managing a sweet shop's inventory, sales, and customer interactions.

## 🚀 Features

### **Customer Features**
- **User Registration & Login**: Secure authentication with JWT tokens
- **Sweet Browsing**: View available sweets with details
- **Search & Filter**: Find sweets by name, category, or price range
- **Purchase System**: Buy sweets with quantity selection
- **Real-time Updates**: Live inventory updates after purchases

### **Admin Features**
- **Admin Panel**: Full administrative interface
- **Sweet Management**: Add, edit, and delete sweets
- **Inventory Control**: Restock and track quantities
- **User Management**: View registered users
- **Sales Tracking**: Monitor purchase history

## 🛠️ Technical Stack

### **Backend**
- **FastAPI**: Modern, fast web framework for building APIs
- **MongoDB**: NoSQL database for flexible data storage
- **JWT Authentication**: Secure token-based authentication
- **Pydantic**: Data validation and serialization
- **Bcrypt**: Password hashing for security
- **Uvicorn**: ASGI server for production deployment

### **Frontend**
- **React 18**: Modern JavaScript library for building UIs
- **React Router**: Client-side routing
- **Context API**: State management
- **Axios**: HTTP client for API communication
- **CSS3**: Modern styling with responsive design

### **Development Tools**
- **pytest**: Python testing framework
- **pytest-asyncio**: Async testing support
- **ESLint**: JavaScript linting
- **Git**: Version control

## 📁 Project Structure

```
Sweet-shop/
├── backend/                 # FastAPI backend
│   ├── routers/            # API route handlers
│   │   ├── auth.py         # Authentication endpoints
│   │   ├── sweets.py       # Sweet management endpoints
│   │   └── inventory.py    # Inventory management endpoints
│   ├── tests/              # Test suite
│   ├── models.py           # Pydantic data models
│   ├── auth.py             # Authentication utilities
│   ├── database.py         # MongoDB connection
│   └── main.py             # FastAPI application
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── contexts/       # Context providers
│   │   └── App.js          # Main application
│   └── package.json        # Dependencies
├── start.sh               # Development startup script
├── test_system.py         # End-to-end testing
└── README.md              # This file
```

## 🚀 Quick Start

### **Prerequisites**
- Python 3.11+
- Node.js 16+
- MongoDB
- Git

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd Sweet-shop
```

### **2. Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Frontend Setup**
```bash
cd frontend
npm install
```

### **4. Start MongoDB**
Make sure MongoDB is running on your system.

### **5. Run the Application**
```bash
# Option 1: Use the startup script
./start.sh

# Option 2: Manual startup
# Terminal 1 - Backend
cd backend && source venv/bin/activate && uvicorn main:app --reload

# Terminal 2 - Frontend  
cd frontend && npm start
```

### **6. Access the Application**
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 👤 Default Admin Account

- **Username**: `admin`
- **Password**: `admin123`

## 🧪 Testing

### **Backend Tests**
```bash
cd backend
source venv/bin/activate
pytest
```

### **Frontend Tests**
```bash
cd frontend
npm test
```

### **End-to-End Testing**
```bash
python test_system.py
```

## 📚 API Documentation

### **Authentication Endpoints**
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### **Sweet Management Endpoints**
- `GET /api/sweets/` - Get all sweets
- `GET /api/sweets/search` - Search sweets
- `POST /api/sweets/` - Create sweet (Admin only)
- `PUT /api/sweets/{id}` - Update sweet (Admin only)
- `DELETE /api/sweets/{id}` - Delete sweet (Admin only)

### **Inventory Endpoints**
- `POST /api/sweets/{id}/purchase` - Purchase sweet
- `POST /api/sweets/{id}/restock` - Restock sweet (Admin only)

## 🔧 Development

### **Adding New Features**
1. Write tests first (TDD approach)
2. Implement the feature
3. Ensure all tests pass
4. Commit with descriptive message

### **Code Style**
- Python: Follow PEP 8
- JavaScript: Use ESLint configuration
- Commits: Use conventional commit messages

### **Database Seeding**
```bash
python add_sample_data.py
```

## 🚀 Deployment

### **Backend Deployment**
1. Set up production MongoDB
2. Configure environment variables
3. Use production ASGI server (Gunicorn + Uvicorn)
4. Set up reverse proxy (Nginx)

### **Frontend Deployment**
1. Build production bundle: `npm run build`
2. Serve static files with web server
3. Configure API endpoints for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Ensure all tests pass
6. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🎯 Development Journey

This project was built using **Test-Driven Development (TDD)** methodology:

1. **Initial Setup**: Project structure and Git repository
2. **Backend Development**: FastAPI + MongoDB implementation
3. **Test Suite**: Comprehensive testing framework
4. **Frontend Development**: React SPA with modern UI
5. **Integration**: Full-stack integration and testing
6. **Bug Fixes**: Model validation and admin panel fixes
7. **Documentation**: Comprehensive README and API docs

## 🏆 Achievements

- ✅ Full-stack application with modern tech stack
- ✅ Test-driven development methodology
- ✅ Responsive and intuitive user interface
- ✅ Secure authentication and authorization
- ✅ Real-time inventory management
- ✅ Comprehensive API documentation
- ✅ Production-ready codebase
- ✅ Git version control with descriptive commits

## 🤖 My AI Usage

This project was developed with AI assistance as a helpful tool to enhance productivity and code quality.

### **AI Assistance Areas**
- **Code Suggestions**: AI provided code templates and suggestions for backend API structure, React components, and database models
- **Problem Solving**: AI helped with debugging, error resolution, and compatibility fixes
- **Documentation**: AI assisted in generating comprehensive README, API docs, and test reports
- **Testing**: AI generated comprehensive test cases and validation strategies

