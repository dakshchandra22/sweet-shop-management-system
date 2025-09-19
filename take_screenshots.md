# 📸 Screenshot Guide for Sweet Shop

## Quick Screenshot Checklist

### 1. **Login Page** (`login.png`)
- **URL**: http://localhost:3000
- **What to capture**: 
  - Purple gradient background
  - "Login to Sweet Shop" header
  - Username and password fields
  - "Login" button
  - "Register here" link

### 2. **Registration Page** (`register.png`)
- **URL**: Click "Register here" from login page
- **What to capture**:
  - Purple gradient background
  - "Register for Sweet Shop" header
  - Email, username, password fields
  - Password strength indicator
  - "Register" button
  - "Login here" link

### 3. **Customer Dashboard** (`customer-dashboard.png`)
- **URL**: Login as regular user (not admin)
- **What to capture**:
  - "Welcome to Sweet Shop" header
  - Search bar with "Search sweets..." placeholder
  - Sort buttons (Low to High, High to Low)
  - Product cards with purchase buttons
  - Stock quantities

### 4. **Admin Dashboard** (`admin-dashboard.png`)
- **URL**: Login as admin user
- **What to capture**:
  - "Hello admin" with yellow "Admin" badge
  - "➕ Add New Sweet" button
  - Product cards with "Edit" and "Delete" buttons
  - Stock management controls

### 5. **Add New Sweet Modal** (`add-sweet-modal.png`)
- **URL**: Click "➕ Add New Sweet" button (admin only)
- **What to capture**:
  - Modal popup with purple header
  - "Add New Sweet" title
  - Name, Category, Price, Quantity fields
  - "Cancel" and "Add Sweet" buttons

### 6. **Search Results** (`search-results.png`)
- **URL**: Type something in search box and click "Search"
- **What to capture**:
  - Search bar with query text
  - Filtered product results
  - "Clear" button

### 7. **Full Product Grid** (`product-grid.png`)
- **URL**: Clear search to show all products
- **What to capture**:
  - Complete grid of all available sweets
  - Multiple rows of product cards
  - All product information visible

## 📱 Screenshot Settings

### Recommended Settings:
- **Resolution**: 1920x1080 (Full HD)
- **Format**: PNG (for best quality)
- **Browser**: Chrome or Firefox
- **Viewport**: Use browser dev tools to set exact size

### Browser Dev Tools Setup:
1. Open Developer Tools (F12)
2. Click device toolbar icon (📱)
3. Set custom dimensions: 1920 x 1080
4. Refresh page
5. Take screenshot

## 🚀 Quick Commands

### Start the Application:
```bash
# Terminal 1 - Backend
cd backend
uvicorn main:app --reload

# Terminal 2 - Frontend  
cd frontend
npm start
```

### Test Users:
- **Admin**: username: `admin`, password: `admin123`
- **Customer**: Register a new account

### Screenshot Tools:
- **Mac**: Cmd+Shift+4 (select area) or Cmd+Shift+3 (full screen)
- **Windows**: Windows+Shift+S (Snipping Tool)
- **Browser**: Right-click → "Save as image" or use extensions

## 📁 File Organization

After taking screenshots, organize them like this:
```
screenshots/
├── login.png
├── register.png
├── customer-dashboard.png
├── admin-dashboard.png
├── add-sweet-modal.png
├── search-results.png
└── product-grid.png
```

## 🔗 Update README URLs

After uploading to GitHub, update the README.md with your actual repository URL:

```markdown
# Replace this:
https://raw.githubusercontent.com/yourusername/sweet-shop/main/screenshots/login.png

# With your actual URL:
https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/main/screenshots/login.png
```

## ✅ Quality Checklist

- [ ] All screenshots are 1920x1080 resolution
- [ ] Images are clear and not blurry
- [ ] All UI elements are visible
- [ ] Colors and gradients are properly displayed
- [ ] Text is readable
- [ ] No browser UI elements (address bar, bookmarks) visible
- [ ] Screenshots show actual functionality, not placeholder content

## 🎯 Pro Tips

1. **Use incognito mode** to avoid browser extensions interfering
2. **Clear browser cache** before taking screenshots
3. **Test on different screen sizes** if possible
4. **Take multiple shots** and choose the best one
5. **Ensure consistent styling** across all screenshots
6. **Include real data** in the screenshots (not just placeholders)

---

**Ready to take screenshots?** Start with the login page and work through the list! 📸
