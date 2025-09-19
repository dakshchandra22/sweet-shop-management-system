# 🍭 Sweet Shop - Super Simple Guide

A beginner-friendly e-commerce app for selling sweets!

## 🚀 Quick Start

### Option 1: Easy Way (Recommended)
```bash
chmod +x start.sh
./start.sh
```

### Option 2: Manual Way
```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm start
```

## 📁 What Each File Does

### Backend (Python)
- **main.py** - Starts the server
- **models.py** - Defines data shapes (User, Sweet, etc.)
- **database.py** - Saves/gets data from MongoDB
- **auth.py** - Handles login/logout
- **sweets.py** - Manages sweet operations
- **routes.py** - API endpoints (URLs)

### Frontend (React)
- **App.js** - Main app component
- **components/** - UI pieces
  - **SweetShop.js** - Main page controller
  - **Header.js** - Top navigation
  - **Login.js** - Login form
  - **Register.js** - Sign up form
  - **SearchBar.js** - Search and filters
  - **SweetCard.js** - Individual sweet display
  - **SweetForm.js** - Add/edit sweet form
  - **SweetList.js** - Grid of sweets

## 🎯 How It Works

1. **User visits website** → Sees login page
2. **User logs in** → Goes to main shop page
3. **User browses sweets** → Can search and sort
4. **User buys sweet** → Quantity decreases
5. **Admin adds sweets** → New sweets appear

## 🔑 User Types

### Customer
- Register/Login
- Browse sweets
- Search and sort
- Buy sweets

### Admin
- Everything customers can do
- Add new sweets
- Edit existing sweets
- Delete sweets
- Restock inventory

## 🧪 Testing

### Backend Tests
```bash
cd backend
python test_simple_tdd.py
```

### Frontend Tests
```bash
open frontend/run_tests.html
```

## 🛠️ Common Tasks

### Add a New Sweet (Admin)
1. Login as admin
2. Click "Add New Sweet" button
3. Fill in the form
4. Click "Add Sweet"

### Buy a Sweet (Customer)
1. Login as customer
2. Find the sweet you want
3. Enter quantity
4. Click "Purchase"

### Search Sweets
1. Type in search box
2. Click "Search" button
3. Or use sort buttons

## 🚨 Troubleshooting

### Backend Won't Start
- Check if port 8000 is free
- Make sure MongoDB is running
- Check if all packages are installed

### Frontend Won't Start
- Check if port 3000 is free
- Run `npm install` first
- Check if Node.js is installed

### Can't Login
- Check if backend is running
- Try username: `admin`, password: `admin123`
- Check browser console for errors

## 📚 Learning Tips

1. **Start with main.py** - See how the server starts
2. **Look at models.py** - Understand data structure
3. **Check routes.py** - See available API endpoints
4. **Examine App.js** - See how React components connect
5. **Follow one feature** - Like user login from start to finish

## 🎨 Customization

### Change Colors
- Edit the gradient colors in components
- Look for `linear-gradient` in the code

### Add New Features
1. Add new function in backend
2. Add new API route
3. Add new React component
4. Connect everything together

## 📞 Need Help?

1. Check the browser console for errors
2. Check the terminal where backend is running
3. Look at the test files to understand expected behavior
4. Read the comments in the code - they explain everything!

## 🎉 You're Ready!

The code is now super simple and beginner-friendly. Every file has clear comments explaining what it does. Start with `main.py` and `App.js` to understand the flow, then explore other files as needed!