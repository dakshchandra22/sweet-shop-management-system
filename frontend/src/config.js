// Frontend Configuration
const config = {
  // API Configuration
  API_BASE_URL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api',
  
  // Application Configuration
  APP_NAME: 'Sweet Shop Management System',
  VERSION: '1.0.0',
  
  // Feature Flags
  ENABLE_REGISTRATION: process.env.REACT_APP_ENABLE_REGISTRATION !== 'false',
  ENABLE_ADMIN_PANEL: process.env.REACT_APP_ENABLE_ADMIN_PANEL !== 'false',
  
  // UI Configuration
  ITEMS_PER_PAGE: parseInt(process.env.REACT_APP_ITEMS_PER_PAGE) || 12,
  DEBOUNCE_DELAY: parseInt(process.env.REACT_APP_DEBOUNCE_DELAY) || 300,
};

export default config;
