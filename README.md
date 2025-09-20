# 🍭 Sweet Shop Management System

A full-stack web application built with **Test-Driven Development (TDD)** methodology for managing a sweet shop's inventory, sales, and customer interactions.

## 🛠️ Admin
<img src="https://github.com/user-attachments/assets/ddb23849-9763-4606-9d88-aa0537b88e6d" width="400" alt="Login"> <img src="https://github.com/user-attachments/assets/d4af8214-027b-4f51-9270-1026cc09c5cf"  width="400" alt="Admin Dashboard"> 
 <img src="https://github.com/user-attachments/assets/8553f6f7-b3a8-4815-b9e1-995825644e6a" width="400" alt="Add Sweet Modal">
 
 - **Admin**: `admin` / `admin123` (Full access)

## 🛠️ User
<img src="https://github.com/user-attachments/assets/ddb23849-9763-4606-9d88-aa0537b88e6d" width="400" alt="Login">  <img src="https://github.com/user-attachments/assets/eef0b926-0ac7-4b42-9863-c227fee90a99"  width="400" alt="Register"> 
<img src="https://github.com/user-attachments/assets/ce720015-1ae9-4698-8e5f-08676b417d1f" width="400" alt="Customer Dashboard">  <img src="https://github.com/user-attachments/assets/86fd2438-e030-4933-8a4d-4cf0073c76be" width="400" alt="Product Grid"> <img src="https://github.com/user-attachments/assets/2c4c3001-1000-4be6-ae24-8f28382a886c" width="400" alt="Search Results">  
- **User**: `daksh22_new` / `TestPassword123!` (Customer access)

## 🚀 Features  

**Customer**: Browse sweets, search/filter, purchase with quantity selection  
**Admin**: Full CRUD operations, inventory management, user oversight

## 🛠️ Tech Stack

**Backend**: FastAPI + MongoDB + JWT + Pydantic + Bcrypt  
**Frontend**: React 18 + Context API + Axios + Bootstrap  
**Testing**: pytest + Jest + React Testing Library

## 📁 Project Structure

```
Sweet-shop 7/
├── backend/                    # FastAPI Backend
│   ├── models.py              # Data models
│   ├── auth.py                # Authentication
│   ├── database.py            # MongoDB operations
│   ├── sweets.py              # Sweet management
│   ├── routes.py              # API endpoints
│   ├── main.py                # App entry point
│   ├── simple_categories.py   # TDD Categories
│   ├── simple_routes.py       # TDD Routes
│   └── tests/                 # Test suite
├── frontend/                  # React Frontend
│   ├── src/components/        # React components
│   ├── src/contexts/          # State management
│   ├── src/__tests__/         # Frontend tests
│   └── package.json           # Dependencies
├── .github/workflows/         # CI/CD
├── start.sh                   # Startup script
├── stop.sh                    # Stop script
└── README.md                  # Documentation
```

## 🎯 User Views

**👤 Customer**: Browse sweets, search/filter, purchase with quantity selection  
**👑 Admin**: Full CRUD operations, inventory management, add/edit/delete sweets

## 🚀 Quick Start

```bash
# 1. Clone and setup
git clone <repository-url>
cd Sweet-shop\ 7

# 2. Start application
./start.sh

# 3. Access
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
```
### **Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### **Frontend Setup**
```bash
cd frontend
npm install
npm start
```

**🔑 Login Credentials:**
- **Admin**: `admin` / `admin123` (Full access)
- **User**: `daksh22_new` / `TestPassword123!` (Customer access)

## 📚 API Endpoints

**Auth**: `POST /api/auth/register`, `POST /api/auth/login`  
**Sweets**: `GET /api/sweets/`, `POST /api/sweets/` (Admin), `PUT /api/sweets/{id}` (Admin)  
**Inventory**: `POST /api/sweets/{id}/purchase`, `POST /api/sweets/{id}/restock` (Admin)  
**Categories**: `GET /api/categories`, `POST /api/categories` (Admin)

## 🤖 My AI Usage

## 🤖 How I Used AI Tools

- **Debugging backend:** Helped identify and fix issues in FastAPI routes, JWT authentication flow, and MongoDB integration, speeding up problem-solving without replacing core logic.  
- **Frontend improvements:** Provided design suggestions, UI component ideas, and minor code snippets to enhance user experience and interface consistency.  
- **Testing:** Fully assisted in generating and refining API and frontend test cases, including edge cases and TDD workflows, ensuring high test coverage and meaningful scenarios.  
- **Documentation:** Assisted in structuring the README, setup guides, and overall project explanations to improve clarity, readability, and completeness.  
- **Optimization & validation:** Suggested improvements for password validation, form handling, and API response handling, helping to make the application more robust.  

---

## 🔍 Reflection on AI Usage

- **Impact**: Faster development, cleaner code, better learning  
- **Responsible Use**: Reviewed & tested AI code before use, documented AI help  
- **Key Learning**: AI is best for testing, docs, and debugging → core logic still needs human oversight
