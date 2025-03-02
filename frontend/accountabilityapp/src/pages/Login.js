import React, { useState } from 'react';
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import { useUser } from "../UserContext";
import './Login.css';

function Login() {
    const { setUser } = useUser();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState(null);
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrorMessage(null);

        try {
            const response = await fetch('http://127.0.0.1:5000/loginuser/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const result = await response.json();

            if (response.ok) {
                setUser(result.user);
                navigate('/account');
            } else {
                setErrorMessage(result.message);
            }
        } catch (error) {
            setErrorMessage("Something went wrong. Please try again.");
        }
    };

    return (
        <div>
            <h1 className="title2">AccountAbility</h1>
            <div className="login-container">
                {/* Login Section */}
                <div className="container">
                    <h1 className="title">Login</h1>
                    {errorMessage && <p className="error-message">{errorMessage}</p>}
                    <form className="form" onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label htmlFor="username">Username:</label>
                            <input
                                type="text"
                                id="username"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                        </div>
                        <div className="form-group">
                            <label htmlFor="password">Password:</label>
                            <input
                                type="password"
                                id="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>
                        <button type="submit" className="button">Login</button>
                    </form>
                </div>

                {/* Create Account Section */}
                <div className="container">
                    <h3 className="title">Don't have an account?</h3>
                    <Link to="/createaccount">
                        <button className="button2">Create Account</button>
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default Login;