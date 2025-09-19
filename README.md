# 🍭 Sweet Shop - Complete E-commerce Application

A modern, full-stack e-commerce application for selling sweets with user authentication, admin management, and comprehensive testing. Built with FastAPI backend and React frontend.

## 📸 Screenshots

### Login Page
![Login Page](screenshots/login.png)
*Clean and modern login interface with gradient design*

### Registration Page
![Registration Page](screenshots/register.png)
*Registration form with strong password validation and real-time feedback*

### Customer Dashboard
![Customer Dashboard](screenshots/customer-dashboard.png)
*Customer view with search, sort, and purchase functionality*

### Admin Dashboard
![Admin Dashboard](screenshots/admin-dashboard.png)
*Admin view with full CRUD operations and inventory management*

### Add New Sweet Modal
![Add Sweet Modal](screenshots/add-sweet-modal.png)
*Modal form for adding new sweets (Admin only)*

### Search Results
![Search Results](screenshots/search-results.png)
*Search functionality with filtered results*

### Full Product Grid
![Product Grid](screenshots/product-grid.png)
*Complete product catalog with all available sweets*

## 📚 Understanding the Code Structure

### 🏗️ Project Architecture

```
Sweet-shop 3/
├── backend/                 # Python FastAPI server
│   ├── main.py             # Entry point - starts the server
│   ├── models.py           # Data structures (User, Sweet, etc.)
│   ├── database.py         # Database operations (MongoDB)
│   ├── auth.py             # User authentication & JWT tokens
│   ├── sweets.py           # Sweet management logic
│   ├── routes.py           # API endpoints (URLs)
│   └── test_simple_tdd.py  # Backend tests
├── frontend/               # React application
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── components/     # UI components
│   │   └── contexts/       # State management
│   └── run_tests.html      # Frontend tests
├── start.sh               # Easy startup script
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ 
- Node.js 14+
- MongoDB
- Git

### Option 1: Using the Script (Recommended)
```bash
# Clone the repository
git clone https://github.com/yourusername/sweet-shop.git
cd sweet-shop

# Make script executable and run
chmod +x start.sh
./start.sh
```

### Option 2: Manual Setup

#### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start MongoDB (in a separate terminal)
mongod

# Run the FastAPI server
uvicorn main:app --reload
```

#### Frontend Setup
```bash
# Navigate to frontend directory (in a new terminal)
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
```

#### Access the Application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## 🧪 Testing

### Backend Tests
```bash
cd backend
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
✅ Get sweets works - Found 8 sweets
🔍 Testing purchase sweet...
✅ Purchase sweet works
==================================================
🎉 All tests passed! Backend is working correctly.
```

### Frontend Tests
```bash
open frontend/run_tests.html
```

**Test Coverage:**
- Page loading and rendering
- Component functionality
- API connectivity
- User interactions
- Form validation

## 🧠 Understanding the Code

### Backend (Python + FastAPI)

#### 1. **main.py** - Server Entry Point
```python
from fastapi import FastAPI
from routes import router

app = FastAPI()  # Create web server
app.include_router(router, prefix="/api")  # Add API routes
```
**What it does**: Starts the web server and connects all API routes.

#### 2. **models.py** - Data Structures
```python
class User(BaseModel):
    email: str
    username: str
    password: str
```
**What it does**: Defines the shape of data (like a blueprint for forms).

#### 3. **database.py** - Database Operations
```python
def get_user_by_username(username: str):
    return db.users.find_one({"username": username})
```
**What it does**: Handles all database operations (save, find, update, delete).

#### 4. **auth.py** - User Authentication
```python
def login_user(user: UserLogin) -> TokenResponse:
    # Check password, create JWT token
```
**What it does**: Handles user login, registration, and password security.

#### 5. **sweets.py** - Business Logic
```python
def create_sweet(sweet: Sweet, current_user: str):
    # Check if user is admin, create sweet
```
**What it does**: Contains the business rules (only admins can add sweets).

#### 6. **routes.py** - API Endpoints
```python
@router.post("/sweets")
def add_sweet(sweet: Sweet, current_user: str = Depends(get_user)):
    return create_sweet(sweet, current_user)
```
**What it does**: Defines the URLs that the frontend can call.

### Frontend (React)

#### 1. **App.js** - Main Component
```javascript
function App() {
  return (
    <AuthProvider>
      <SweetProvider>
        <SweetShop />
      </SweetProvider>
    </AuthProvider>
  );
}
```
**What it does**: Sets up the app with user authentication and sweet data management.

#### 2. **contexts/** - State Management
- **AuthContext.js**: Manages user login/logout state
- **SweetContext.js**: Manages sweet data and operations

#### 3. **components/** - UI Components
- **Header.js**: Top navigation bar
- **Login.js**: Login form
- **Register.js**: Registration form
- **SearchBar.js**: Search and filter functionality
- **SweetCard.js**: Individual sweet display
- **SweetForm.js**: Add/Edit sweet form (modal)
- **SweetList.js**: Grid of sweet cards
- **SweetShop.js**: Main page coordinator

## 🔄 How Data Flows

### 1. User Registration
```
Frontend (Register.js) 
    → API Call (/api/auth/register)
    → Backend (routes.py)
    → Auth Logic (auth.py)
    → Database (database.py)
    → MongoDB
```

### 2. User Login
```
Frontend (Login.js)
    → API Call (/api/auth/login)
    → Backend (auth.py)
    → Check Password
    → Return JWT Token
    → Frontend stores token
```

### 3. Adding a Sweet (Admin)
```
Frontend (SweetForm.js)
    → API Call (/api/sweets)
    → Backend (routes.py)
    → Check Admin Permission
    → Save to Database
    → Update Frontend List
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python test_simple_tdd.py
```
**Tests**: Health check, user registration, login, add sweet, get sweets, purchase

### Frontend Tests
```bash
open frontend/run_tests.html
```
**Tests**: Page loading, component rendering, API connectivity, event handling

## 🎯 Key Concepts Explained

### 1. **API (Application Programming Interface)**
- Backend provides URLs that frontend can call
- Example: `GET /api/sweets` returns all sweets
- Example: `POST /api/sweets` creates a new sweet

### 2. **JWT Token (Authentication)**
- When user logs in, backend gives them a "token"
- Frontend sends this token with every request
- Backend checks token to verify user identity

### 3. **State Management (React Context)**
- `AuthContext`: Keeps track of logged-in user
- `SweetContext`: Keeps track of sweets data
- When data changes, all components update automatically

### 4. **Component Structure**
- Each component has one job (Header shows user info, SweetCard shows one sweet)
- Components can be reused (SweetCard used multiple times in SweetList)
- Props pass data from parent to child components

### 5. **Database Operations**
- `find_one()`: Get one record
- `find()`: Get multiple records
- `insert_one()`: Create new record
- `update_one()`: Update existing record
- `delete_one()`: Remove record

## 🔧 Common Tasks

### Adding a New Feature
1. **Backend**: Add function in appropriate file (auth.py, sweets.py, etc.)
2. **Backend**: Add API route in routes.py
3. **Frontend**: Add component or update existing one
4. **Frontend**: Add API call to context
5. **Test**: Add test case

### Debugging
1. **Check browser console** for frontend errors
2. **Check terminal** where backend is running for server errors
3. **Check network tab** in browser for API call failures
4. **Add console.log()** in frontend to see data flow

### Database Issues
1. **Check MongoDB is running**: `mongod`
2. **Check connection string** in database.py
3. **Check if database exists**: `use sweet_shop`

## 📱 User Roles

### Customer
- Register/Login
- Browse sweets
- Search and sort
- Purchase sweets

### Admin
- All customer features
- Add new sweets
- Edit existing sweets
- Delete sweets
- Restock inventory

## 🎨 UI Components Explained

### Bootstrap Classes
- `container`: Centers content
- `row`/`col`: Grid layout
- `btn`: Buttons
- `card`: Content boxes
- `form`: Form elements
- `modal`: Popup windows

### Custom Styling
- Purple gradients for headers
- Pink gradients for sweet cards
- Rounded corners and shadows
- Hover effects

## 🚨 Common Issues

### Backend Won't Start
- Check if port 8000 is free
- Check if all dependencies are installed
- Check if MongoDB is running

### Frontend Won't Start
- Check if port 3000 is free
- Run `npm install` to install dependencies
- Check if Node.js is installed

### API Calls Fail
- Check if backend is running
- Check if CORS is configured
- Check if JWT token is valid

## 📖 Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com/
- **React**: https://reactjs.org/
- **MongoDB**: https://docs.mongodb.com/
- **Bootstrap**: https://getbootstrap.com/

## 🤖 My AI Usage

### AI Tools Used

Throughout the development of this Sweet Shop application, I leveraged several AI tools to enhance my productivity and code quality:

1. **Claude (Anthropic)** - Primary AI assistant for code generation and debugging
2. **GitHub Copilot** - Real-time code suggestions and completions
3. **ChatGPT** - Alternative perspective and code review
4. **Cursor AI** - Integrated AI-powered code editor

### How I Used AI Tools

#### 1. **Code Architecture and Structure**
- **Used Claude to design the overall application architecture** - I asked Claude to help me plan the component structure for both frontend and backend, resulting in a clean separation of concerns with dedicated files for models, database operations, authentication, and business logic.

- **Leveraged AI for API endpoint design** - I used Claude to brainstorm the REST API structure, including endpoint naming conventions, HTTP methods, and response formats. This helped create a consistent and intuitive API design.

#### 2. **Backend Development**
- **FastAPI implementation with AI assistance** - I used Claude to generate the initial FastAPI setup, including CORS middleware configuration, router organization, and dependency injection patterns.

- **Database operations optimization** - Asked Claude to help optimize MongoDB operations and suggest best practices for database connection handling and query patterns.

- **Authentication system development** - Used AI to implement JWT token handling, password hashing with bcrypt, and user role management. Claude helped me understand the security implications and implement proper validation.

- **Error handling and validation** - Leveraged AI to create comprehensive error handling patterns and input validation using Pydantic models.

#### 3. **Frontend Development**
- **React component structure** - Used Claude to design the component hierarchy and state management approach using React Context API instead of more complex state management libraries.

- **Bootstrap integration and styling** - Asked AI to help integrate Bootstrap components and create custom CSS for gradients and modern UI elements.

- **Form validation and user experience** - Used AI to implement real-time password strength validation, form error handling, and user feedback mechanisms.

- **Responsive design implementation** - Leveraged AI suggestions for creating mobile-friendly layouts and responsive grid systems.

#### 4. **Testing and Quality Assurance**
- **TDD implementation** - Used Claude to help design the test-driven development approach, including both backend API tests and frontend component tests.

- **Test case generation** - Asked AI to generate comprehensive test cases covering happy paths, edge cases, and error scenarios.

- **Code refactoring suggestions** - Used AI to identify code smells and suggest improvements for maintainability and performance.

#### 5. **Documentation and README**
- **Comprehensive documentation** - Leveraged AI to create detailed README sections, code comments, and setup instructions.

- **Screenshot descriptions and formatting** - Used AI to help structure the documentation with proper markdown formatting and clear explanations.

### Reflection on AI Impact

#### **Positive Impacts:**

1. **Accelerated Development Speed** - AI tools significantly reduced the time needed for boilerplate code generation, allowing me to focus on business logic and user experience.

2. **Code Quality Improvement** - AI suggestions helped me implement best practices I might have overlooked, such as proper error handling, input validation, and security measures.

3. **Learning Enhancement** - AI explanations helped me understand complex concepts like JWT authentication, React Context API, and FastAPI dependency injection.

4. **Consistent Code Style** - AI tools helped maintain consistent coding patterns throughout the project, making the codebase more maintainable.

5. **Problem-Solving Assistance** - When encountering bugs or implementation challenges, AI provided multiple solution approaches and debugging strategies.

#### **Challenges and Limitations:**

1. **Over-reliance Risk** - I had to be careful not to blindly accept AI suggestions without understanding the underlying concepts and potential security implications.

2. **Context Limitations** - Sometimes AI tools lost context of the overall project structure, requiring me to provide more detailed explanations or break down complex requests.

3. **Code Review Necessity** - AI-generated code still required thorough review and testing to ensure it met project requirements and security standards.

#### **Responsible AI Usage:**

1. **Always reviewed AI-generated code** before implementation
2. **Tested all AI-suggested features** thoroughly before deployment
3. **Maintained understanding** of all implemented solutions
4. **Used AI as a learning tool** rather than a replacement for understanding
5. **Documented AI assistance** transparently in this section

### Key AI-Generated Features

- **Password strength validation system** with real-time feedback
- **Auto-login after registration** functionality
- **Comprehensive error handling** across both frontend and backend
- **Responsive UI components** with Bootstrap integration
- **TDD test suite** covering all major functionality
- **Clean code architecture** with proper separation of concerns

The AI tools were instrumental in creating a professional, secure, and user-friendly e-commerce application while maintaining code quality and following best practices. The combination of AI assistance with careful review and testing resulted in a robust application that demonstrates both technical competence and responsible AI usage.

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact

For questions or support, please open an issue in the GitHub repository.

---

**Note**: This project was developed with AI assistance as documented in the "My AI Usage" section above. All code has been reviewed, tested, and understood before implementation.
