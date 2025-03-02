import logo from './logo.svg';
import './App.css';
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import CreateAccount from './pages/CreateAccount';
import Account from "./pages/Account";

function App() {
  return (
      <Router>
          <Routes>
              <Route path="/" element={<Login />} />
              <Route path="/createaccount" element={<CreateAccount />} />
              <Route path="/account" element={<Account />} />
          </Routes>
      </Router>
  );
}

export default App;