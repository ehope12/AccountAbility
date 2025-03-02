import logo from './logo.svg';
import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import CreateAccount from './pages/CreateAccount';
import Account from "./pages/Account";
import { UserProvider } from "./UserContext"; 

function App() {
  return (
    <UserProvider>
      <Router>
          <Routes>
              <Route path="/" element={<Login />} />
              <Route path="/createaccount" element={<CreateAccount />} />
              <Route path="/account" element={<Account />} />
          </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;