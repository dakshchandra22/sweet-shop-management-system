# Sweet Shop Management System 🍭

A full-stack web application for managing a sweet shop inventory, built with FastAPI (Python) and React (JavaScript) using Test-Driven Development (TDD) methodology.

## Features

### Backend (FastAPI)
- **Authentication**: JWT-based user authentication with registration and login
- **User Management**: Role-based access (Customer/Admin)
- **Sweet Management**: CRUD operations for sweets inventory
- **Inventory Management**: Purchase and restock functionality
- **Database**: MongoDB integration for data persistence
- **API Documentation**: Auto-generated Swagger/OpenAPI docs

### Frontend (React)
- **Modern UI**: Responsive design with beautiful gradients and animations
- **User Authentication**: Login and registration forms
- **Sweet Browsing**: Display all available sweets with search and filter
- **Purchase System**: Buy sweets with quantity selection
- **Admin Panel**: Manage inventory (add, edit, delete, restock sweets)
- **Real-time Updates**: Live inventory updates after purchases/restocks

## Technology Stack

### Backend
- **FastAPI** - Modern, fast web framework for building APIs
- **MongoDB** - NoSQL database for data storage
- **PyMongo** - MongoDB driver for Python
- **JWT** - JSON Web Tokens for authentication
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server for running the application

### Frontend
- **React** - JavaScript library for building user interfaces
- **React Router** - Client-side routing
- **Axios** - HTTP client for API requests
- **CSS3** - Modern styling with gradients and animations

## Project Structure

```
Sweet-shop/
├── backend/
│   ├── routers/
│   │   ├── auth.py          # Authentication endpoints
│   │   ├── sweets.py        # Sweet management endpoints
│   │   └── inventory.py     # Purchase/restock endpoints
│   ├── tests/
│   │   ├── test_auth.py     # Authentication tests
│   │   ├── test_sweets.py   # Sweet management tests
│   │   └── test_inventory.py # Inventory tests
│   ├── main.py              # FastAPI application
│   ├── database.py          # MongoDB connection
│   ├── models.py            # Pydantic models
│   ├── auth.py              # Authentication utilities
│   └── requirements.txt     # Python dependencies
└── frontend/
    ├── src/
    │   ├── components/
    │   │   ├── Navbar.js    # Navigation component
    │   │   ├── Login.js     # Login form
    │   │   ├── Register.js  # Registration form
    │   │   ├── Dashboard.js # Main dashboard
    │   │   ├── AdminPanel.js # Admin interface
    │   │   └── ...          # Other components
    │   ├── contexts/
    │   │   ├── AuthContext.js # Authentication context
    │   │   └── SweetContext.js # Sweet management context
    │   └── App.js           # Main React component
    └── package.json         # Node.js dependencies
```

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- MongoDB (local or cloud instance)

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start MongoDB** (if running locally):
   ```bash
   mongod
   ```

5. **Run the backend server:**
   ```bash
   python run_server.py
   ```

   The API will be available at `http://localhost:8000`
   API documentation at `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

   The application will be available at `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user

### Sweets (Protected)
- `GET /api/sweets/` - Get all sweets
- `GET /api/sweets/search` - Search sweets by name, category, price
- `GET /api/sweets/{id}` - Get specific sweet
- `POST /api/sweets/` - Create new sweet (Admin only)
- `PUT /api/sweets/{id}` - Update sweet (Admin only)
- `DELETE /api/sweets/{id}` - Delete sweet (Admin only)

### Inventory (Protected)
- `POST /api/sweets/{id}/purchase` - Purchase sweet
- `POST /api/sweets/{id}/restock` - Restock sweet (Admin only)

## Testing

### Backend Tests
```bash
cd backend
source venv/bin/activate
python run_tests.py
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Usage

1. **Register/Login**: Create an account or login with existing credentials
2. **Browse Sweets**: View all available sweets on the dashboard
3. **Search & Filter**: Use the search bar to find specific sweets
4. **Purchase**: Select quantity and purchase sweets (reduces inventory)
5. **Admin Functions**: Admin users can manage inventory through the admin panel

## Development Notes

- Built using TDD methodology with comprehensive test coverage
- Simple JWT authentication for easy setup and testing
- Responsive design works on desktop and mobile devices
- Clean, maintainable code following best practices
- Error handling and user feedback throughout the application

## Future Enhancements

- Order history and user profiles
- Payment integration
- Email notifications
- Advanced analytics and reporting
- Multi-language support
- Mobile app development

