# 🍭 Sweet Shop Management System

A full-stack web application built with **Test-Driven Development (TDD)** methodology for managing a sweet shop's inventory, sales, and customer interactions.

## 📸 Screenshots

### Login Page
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/login.png" width="300" alt="Login Page">
*Clean and modern login interface with gradient design*

### Registration Page
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/register.png" width="300" alt="Registration Page">
*Registration form with strong password validation and real-time feedback*

### Customer Dashboard
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/customer-dashboard.png" width="300" alt="Customer Dashboard">
*Customer view with search, sort, and purchase functionality*

### Admin Dashboard
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/admin-dashboard.png" width="300" alt="Admin Dashboard">
*Admin view with full CRUD operations and inventory management*

### Add New Sweet Modal
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/add-sweet-modal.png" width="300" alt="Add Sweet Modal">
*Modal form for adding new sweets (Admin only)*

### Search Results
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/search-results.png" width="300" alt="Search Results">
*Search functionality with filtered results*

### Full Product Grid
<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/product-grid.png" width="300" alt="Product Grid">
*Complete product catalog with all available sweets*

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
- **Bootstrap**: Modern CSS framework for responsive design

### **Development Tools**
- **pytest**: Python testing framework
- **pytest-asyncio**: Async testing support
- **ESLint**: JavaScript linting
- **Git**: Version control

## 📁 Project Structure

```
Sweet-shop 3/
├── backend/                 # FastAPI backend
│   ├── models.py           # Pydantic data models
│   ├── auth.py             # Authentication utilities
│   ├── database.py         # MongoDB connection
│   ├── sweets.py           # Sweet management logic
│   ├── routes.py           # API route handlers
│   ├── main.py             # FastAPI application
│   └── test_simple_tdd.py  # Test suite
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── contexts/       # Context providers
│   │   └── App.js          # Main application
│   └── package.json        # Dependencies
├── screenshots/            # Application screenshots
├── start.sh               # Development startup script
├── TEST_REPORT.md         # Detailed test results
└── README.md              # This file
```

## 🎯 Application Views

### **👤 Customer View (Without Admin Panel)**
When logged in as a regular customer, users see:
- **Dashboard**: Browse all available sweets with search and filter options
- **Sweet Cards**: Each sweet displays name, category, price, and quantity
- **Purchase System**: Quantity selector and purchase button for each sweet
- **Search & Filter**: Filter by name, category, and price range
- **Navigation**: Dashboard and Logout options only

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/customer-dashboard.png" width="300" alt="Customer Dashboard">
*Customer view showing the main dashboard with sweet browsing, search filters, and purchase functionality*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/login.png" width="300" alt="Login Page">
*Clean and modern login interface with gradient design*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/register.png" width="300" alt="Registration Page">
*Registration form with strong password validation and real-time feedback*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/admin-dashboard.png" width="300" alt="Admin Dashboard">
*Admin view with full CRUD operations and inventory management*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/add-sweet-modal.png" width="300" alt="Add Sweet Modal">
*Modal form for adding new sweets (Admin only)*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/search-results.png" width="300" alt="Search Results">
*Search functionality with filtered results*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/product-grid.png" width="300" alt="Product Grid">
*Complete product catalog with all available sweets*

**Features Available:**
- View all sweets in an attractive grid layout
- Search sweets by name or category
- Filter by price range (min/max)
- Purchase sweets with quantity selection
- Real-time inventory updates after purchase

### **👑 Admin View (With Admin Panel)**
When logged in as an admin user, users see:
- **Dashboard**: Same customer view for browsing sweets
- **Admin Panel**: Full inventory management interface
- **Sweet Management**: Add, edit, and delete sweets
- **Inventory Control**: Restock sweets and manage quantities
- **Navigation**: Dashboard, Admin Panel, and Logout options

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/admin-dashboard.png" width="300" alt="Admin Panel">
*Admin panel showing inventory management with add, edit, delete, and restock functionality*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/add-sweet-modal.png" width="300" alt="Edit Sweet Modal">
*Admin interface for editing sweet details with form validation*

**Additional Admin Features:**
- **Add New Sweet**: Form to create new sweet items
- **Edit Sweet**: Modify existing sweet details (name, category, price, quantity)
- **Delete Sweet**: Remove sweets from inventory
- **Restock**: Increase quantity of existing sweets
- **Full CRUD Operations**: Complete control over sweet inventory

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- Node.js 14+
- MongoDB
- Git

### **1. Clone the Repository**
   ```bash
git clone <repository-url>
cd Sweet-shop 3
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

### **7. Quick Login**
- **Admin**: `admin` / `admin123` (Full access)
- **User**: `user` / `user123` (Customer access)
- **Test**: `testuser` / `TestPass123!` (Customer access)

## 👤 User Accounts

### **Admin Account**
- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Full administrative control, can add/edit/delete sweets, manage inventory

### **Regular User Account**
- **Username**: `user`
- **Password**: `user123`
- **Access**: Customer features only, can browse and purchase sweets

### **Test User Account**
- **Username**: `testuser`
- **Password**: `TestPass123!`
- **Access**: Customer features only, for testing purposes

### **User Registration Process**
The application supports user registration with the following features:

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/register.png" width="300" alt="User Registration">
*User registration form with email, username, and password fields*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/customer-dashboard.png" width="300" alt="Registration Success">
*Successful registration confirmation and automatic login*

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/customer-dashboard.png" width="300" alt="User Dashboard">
*New user dashboard showing available sweets and purchase options*

**Registration Features:**
- **Email Validation**: Ensures valid email format
- **Username Uniqueness**: Prevents duplicate usernames
- **Password Security**: Strong password requirements with real-time validation
- **Automatic Login**: Users are automatically logged in after registration
- **Role Assignment**: Regular users get customer access, specific usernames get admin access

## 🔄 Testing Different User Views

### **Testing Customer View**
1. Register a new user account OR use the test accounts:
   - **User**: `user` / `user123`
   - **Test**: `testuser` / `TestPass123!`
2. Login with the account
3. You'll see only the Dashboard and Logout options
4. Browse sweets, search, filter, and make purchases
5. No admin panel access - only customer features

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/login.png" width="300" alt="Login Page">
*Clean login interface with username and password fields*

### **Testing Admin View**
1. Login with the admin account (admin/admin123)
2. You'll see Dashboard, Admin Panel, and Logout options
3. Click "➕ Add New Sweet" to access inventory management
4. Add, edit, delete, and restock sweets
5. Full administrative control over the system

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/admin-dashboard.png" width="300" alt="Admin Dashboard">
*Admin view showing both customer dashboard and admin panel access*

### **Role-Based Access Control**
- **Regular Users**: Can only view and purchase sweets
- **Admin Users**: Can manage inventory, add/edit/delete sweets, and restock
- **Automatic Detection**: System automatically detects admin status based on username

## 🧪 Testing

### **Backend Tests**
   ```bash
cd backend
source venv/bin/activate
python test_simple_tdd.py
```

**Test Results:**
```
🚀 Starting Simple TDD Tests for Sweet Shop Backend
==================================================
🔍 Testing backend health...
✅ Backend is running
🔍 Testing user registration...
✅ User registration works
🔍 Testing user login...
✅ User login works
🔍 Testing add sweet...
✅ Add sweet works
🔍 Testing get sweets...
✅ Get sweets works - Found 14 sweets
🔍 Testing purchase sweet...
✅ Purchase sweet works
==================================================
🎉 All tests passed! Backend is working correctly.
```

### **Frontend Tests**
   ```bash
open frontend/run_tests.html
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

This project was developed with strategic AI assistance primarily for testing and documentation.

### **AI Tools Used**
1. **Claude (Anthropic)** - Primary AI assistant for testing and documentation
2. **GitHub Copilot** - Occasional code suggestions and completions
3. **ChatGPT** - Alternative perspective for problem-solving
4. **Cursor AI** - Integrated AI-powered code editor

### **AI Assistance Areas**
- **Testing**: AI helped generate comprehensive test cases and identify edge cases for both backend API endpoints and frontend functionality
- **Documentation**: AI assisted in creating detailed README sections, test reports, and code explanations
- **Problem Solving**: AI provided debugging assistance and alternative solution approaches
- **Code Review**: AI offered suggestions for code structure and best practices

### **Responsible AI Usage**
- **Primarily used AI for testing and documentation** rather than core development
- **Always reviewed AI-generated code** before implementation
- **Tested all AI-suggested features** thoroughly before deployment
- **Maintained understanding** of all implemented solutions
- **Used AI as a learning tool** rather than a replacement for understanding
- **Documented AI assistance** transparently in this section

The core application logic and architecture were primarily developed through traditional programming approaches, with AI serving as a helpful assistant for specific tasks rather than the primary development tool.

## 📞 Contact

For questions or support, please open an issue in the GitHub repository.

---

**Note**: This project was developed with strategic AI assistance primarily for testing and documentation as documented in the "My AI Usage" section above. All code has been reviewed, tested, and understood before implementation.