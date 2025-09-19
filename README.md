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

## 📁 Structure

```
Sweet-shop 3/
├── backend/          # FastAPI + MongoDB
├── frontend/         # React + Bootstrap  
├── start.sh         # Quick start script
└── README.md        # Documentation
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

**Login Credentials:**
- **Admin**: `admin` / `admin123`
- **User**: `user` / `user123`

## 📚 API Endpoints

**Auth**: `POST /api/auth/register`, `POST /api/auth/login`  
**Sweets**: `GET /api/sweets/`, `POST /api/sweets/` (Admin), `PUT /api/sweets/{id}` (Admin)  
**Inventory**: `POST /api/sweets/{id}/purchase`, `POST /api/sweets/{id}/restock` (Admin)

## 🤖 AI Usage

**Tools**: Claude, GitHub Copilot, ChatGPT, Cursor AI  
**Usage**: Testing, documentation, debugging assistance  
**Approach**: AI as assistant for specific tasks, not primary development tool
