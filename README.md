# 🍭 Sweet Shop Management System

A full-stack web application built with **Test-Driven Development (TDD)** methodology for managing a sweet shop's inventory, sales, and customer interactions.

## 📸 Screenshots

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/login.png" width="200" alt="Login"> <img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/register.png" width="200" alt="Register"> <img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/customer-dashboard.png" width="200" alt="Customer Dashboard">

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/admin-dashboard.png" width="200" alt="Admin Dashboard"> <img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/add-sweet-modal.png" width="200" alt="Add Sweet Modal"> <img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/search-results.png" width="200" alt="Search Results">

<img src="https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/product-grid.png" width="200" alt="Product Grid">

## 🚀 Features

**Customer**: Browse sweets, search/filter, purchase with quantity selection  
**Admin**: Full CRUD operations, inventory management, user oversight

## 🛠️ Tech Stack

**Backend**: FastAPI + MongoDB + JWT + Pydantic + Bcrypt  
**Frontend**: React 18 + Context API + Axios + Bootstrap  
**Testing**: pytest + ESLint

## 📁 Project Structure

```
Sweet-shop 3/
├── backend/                    # FastAPI Backend
│   ├── models.py              # Data models
│   ├── auth.py                # Authentication
│   ├── database.py            # MongoDB operations
│   ├── sweets.py              # Sweet management
│   ├── routes.py              # API endpoints
│   ├── main.py                # App entry point
│   └── test_simple_tdd.py     # Tests
├── frontend/                  # React Frontend
│   ├── src/components/        # React components
│   ├── src/contexts/          # State management
│   └── package.json           # Dependencies
├── screenshots/               # App screenshots
├── start.sh                   # Startup script
└── README.md                  # Documentation
```

## 🎯 User Views

**👤 Customer**: Browse sweets, search/filter, purchase with quantity selection  
**👑 Admin**: Full CRUD operations, inventory management, add/edit/delete sweets

## 🚀 Quick Start

```bash
# 1. Clone and setup
git clone <repository-url>
cd Sweet-shop\ 3

# 2. Start application
./start.sh

# 3. Access
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
```

**🔑 Login Credentials:**
- **Admin**: `admin` / `admin123` (Full access)
- **User**: `user` / `user123` (Customer access)

## 📚 API Endpoints

**Auth**: `POST /api/auth/register`, `POST /api/auth/login`  
**Sweets**: `GET /api/sweets/`, `POST /api/sweets/` (Admin), `PUT /api/sweets/{id}` (Admin)  
**Inventory**: `POST /api/sweets/{id}/purchase`, `POST /api/sweets/{id}/restock` (Admin)

## 🤖 My AI Usage

This project was developed with strategic AI assistance, primarily for testing, documentation, and problem-solving. Here's a detailed breakdown of how AI tools were leveraged:

### **AI Tools Used**

1. **Claude (Anthropic)** - Primary AI assistant for comprehensive project support
2. **GitHub Copilot** - Code completion and suggestions during development
3. **ChatGPT** - Alternative perspective for debugging and architecture decisions
4. **Cursor AI** - Integrated AI-powered code editor for real-time assistance

### **How I Used AI Tools**

#### **Testing & Quality Assurance**
- **Claude**: Generated comprehensive test cases for both backend API endpoints and frontend components
- **Example**: "I used Claude to create the `test_simple_tdd.py` file with 6 comprehensive test cases covering user registration, login, sweet management, and purchase functionality"
- **Claude**: Identified edge cases and potential failure points in the authentication system
- **Example**: "I asked Claude to help debug password validation issues and JWT token handling"

#### **Documentation & README**
- **Claude**: Assisted in creating detailed project documentation and README sections
- **Example**: "I used Claude to structure the README.md with proper sections, screenshots, and setup instructions"
- **Claude**: Helped write clear explanations of the tech stack and project architecture

#### **Frontend Development**
- **Cursor AI**: Provided real-time code suggestions for React components
- **Example**: "I used Cursor AI to help implement the Bootstrap modal for adding new sweets"
- **GitHub Copilot**: Assisted with React Context API implementation and state management
- **Example**: "Copilot helped generate the authentication context and sweet management context"

#### **Backend Development**
- **Claude**: Helped debug FastAPI route handlers and MongoDB integration
- **Example**: "I used Claude to troubleshoot the JWT authentication middleware and password hashing"
- **ChatGPT**: Provided alternative approaches for API endpoint design
- **Example**: "I asked ChatGPT for suggestions on structuring the REST API endpoints for sweet management"

#### **Problem Solving & Debugging**
- **Claude**: Assisted in resolving connection issues between frontend and backend
- **Example**: "I used Claude to diagnose and fix the 'connection refused' error when the frontend couldn't reach the backend API"
- **Claude**: Helped optimize the password validation logic to be more user-friendly
- **Example**: "I asked Claude to modify the password requirements from 'all 4 criteria' to '3 out of 4 criteria' for better UX"

### **My Reflection on AI Impact**

#### **Positive Impacts**
- **Faster Development**: AI significantly accelerated the testing and documentation phases
- **Better Code Quality**: AI suggestions helped identify potential bugs and improve code structure
- **Learning Enhancement**: AI explanations helped me understand complex concepts like JWT authentication and React Context API
- **Efficiency**: Reduced time spent on repetitive tasks like writing test cases and documentation

#### **Responsible Usage**
- **Always Reviewed AI Code**: I never implemented AI-generated code without understanding and testing it first
- **Maintained Control**: Used AI as a tool to enhance my work, not replace my decision-making
- **Transparent Documentation**: Documented all AI assistance openly in this section
- **Learning-Focused**: Used AI to learn new concepts rather than just copy-paste solutions

#### **Workflow Integration**
- **Iterative Process**: Used AI for initial drafts, then refined and customized the output
- **Validation**: Always tested AI suggestions thoroughly before implementation
- **Collaboration**: Treated AI as a coding partner, asking clarifying questions and seeking alternatives
- **Quality Assurance**: Used AI to review my own code and suggest improvements

### **Key Learnings**
- **AI is most effective** for testing, documentation, and debugging rather than core architecture decisions
- **Human oversight is crucial** - AI suggestions need validation and customization
- **AI accelerates learning** but doesn't replace understanding the underlying concepts
- **Transparency matters** - documenting AI usage builds trust and shows responsible development practices

This project demonstrates how AI can be leveraged effectively as a development assistant while maintaining full understanding and control over the codebase.
