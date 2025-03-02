import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useUser } from "../UserContext";
import './CreateAccount.css';

function CreateAccount() {
    const { setUser } = useUser();
    const navigate = useNavigate();
    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const [streetnumber, setStreetnumber] = useState('');
    const [streetname, setStreetname] = useState('');
    const [city, setCity] = useState('');
    const [state, setState] = useState('ex. IL');
    const [zipcode, setZipcode] = useState('');
    const [balance, setBalance] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null);

    const handleSubmit = async (event) => {
        event.preventDefault();
        setErrorMessage(null);
        setSuccessMessage(null);
        console.log('Signing up with:', firstname, lastname, streetnumber, streetname, city, state, zipcode, balance, username, password);
        const userData = {
            firstname,
            lastname,
            address: [streetnumber, streetname, city, state, zipcode],
            balance,
            username,
            password
        }
        try {
            const response = await fetch('http://127.0.0.1:5000/createuser/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(userData)
            });

            const result = await response.json();

            if (response.ok) {
                setSuccessMessage(result.message);
                setUser(result.user);
                navigate('/account');
            } else {
                setErrorMessage(result.message);
            }
        } catch (error) {
            setErrorMessage("Error creating user");
        }
    };

    return (
        <div>
            <h1>Get Started With AccountAbility</h1>
            <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="firstname">First Name:</label>
                <input
                type="text"
                id="firstname"
                value={firstname}
                onChange={(e) => setFirstname(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="lastname">Last Name:</label>
                <input
                type="text"
                id="lastname"
                value={lastname}
                onChange={(e) => setLastname(e.target.value)}
                />
            </div>
            <h3>Address Information</h3>
            <div>
                <label htmlFor="streetnumber">Address Number:</label>
                <input
                type="text"
                id="streetnumber"
                value={streetnumber}
                onChange={(e) => setStreetnumber(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="streetname">Street Name:</label>
                <input
                type="text"
                id="streetname"
                value={streetname}
                onChange={(e) => setStreetname(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="city">City:</label>
                <input
                type="text"
                id="city"
                value={city}
                onChange={(e) => setCity(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="streetname">State:</label>
                <input
                type="text"
                id="state"
                value={state}
                onChange={(e) => setState(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="zipcode">Zipcode:</label>
                <input
                type="text"
                id="zipcode"
                value={zipcode}
                onChange={(e) => setZipcode(e.target.value)}
                />
            </div>
            <h3>Initial Account Balance</h3>
            <div>
                <label htmlFor="balance">Balance:</label>
                <input
                type="text"
                id="balance"
                value={balance}
                onChange={(e) => setBalance(e.target.value)}
                />
            </div>
            <h3>Account Information</h3>
            <div>
                <label htmlFor="username">Username:</label>
                <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="password">Password:</label>
                <input
                type="password"
                id="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button type="submit">Sign Up</button>
            </form>
        </div>
    );
}

export default CreateAccount;