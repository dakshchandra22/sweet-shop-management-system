import React from 'react';
import { AuthProvider } from './contexts/AuthContext';
import { SweetProvider } from './contexts/SweetContext';
import SweetShop from './components/SweetShop';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <SweetProvider>
        <SweetShop />
      </SweetProvider>
    </AuthProvider>
  );
}

export default App;