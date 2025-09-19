# 🍭 Sweet Shop Management System

A full-stack web application built with **Tes t-Driven Development (TDD)** methodology for managing a sweet shop's inventory, sales, and customer interactions.

<img src="https://github.com/user-attachments/assets/ddb23849-9763-4606-9d88-aa0537b88e6d" width="500" alt="Login">  <img  src="https://github.com/user-attachments/assets/eef0b926-0ac7-4b42-9863-c227fee90a99"  width="500" alt="Register"> 
<img src="https://github.com/user-attachments/assets/ce720015-1ae9-4698-8e5f-08676b417d1f" width="500" alt="Customer Dashboard">  <img src="https://github.com/user-attachments/assets/d4af8214-027b-4f51-9270-1026cc09c5cf"  width="500" alt="Admin Dashboard">  <img src="https://github.com/user-attachments/assets/8553f6f7-b3a8-4815-b9e1-995825644e6a" width="500" alt="Add Sweet Modal">  <img src="https://github.com/user-attachments/assets/2c4c3001-1000-4be6-ae24-8f28382a886c" width="500" alt="Search Results">  <img src="https://github.com/user-attachments/assets/86fd2438-e030-4933-8a4d-4cf0073c76be" width="500" alt="Product Grid">

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
- **User**: `daksh2004` / `Daksh@22` (Customer access)

## 📚 API Endpoints

**Auth**: `POST /api/auth/register`, `POST /api/auth/login`  
**Sweets**: `GET /api/sweets/`, `POST /api/sweets/` (Admin), `PUT /api/sweets/{id}` (Admin)  
**Inventory**: `POST /api/sweets/{id}/purchase`, `POST /api/sweets/{id}/restock` (Admin)

## 🤖 My AI Usage

## 🤖 How I Used AI Tools

- **Frontend**: Used *Cursor AI* and *GitHub Copilot* for React components, authentication, and UI improvements  
- **Backend**: Used *Claude* and *ChatGPT* to debug FastAPI routes, JWT auth, and MongoDB integration  
- **Testing**: Generated and refined API & frontend test cases with *Claude*  
- **Docs**: Structured `README.md`, setup guide, and project explanation using *Claude*  
- **Debugging**: Fixed frontend–backend API connection issues and optimized password validation  

---

## 🔍 Reflection on AI Usage

- **Impact**: Faster development, cleaner code, better learning  
- **Responsible Use**: Reviewed & tested AI code before use, documented AI help  
- **Key Learning**: AI is best for testing, docs, and debugging → core logic still needs human oversight  
