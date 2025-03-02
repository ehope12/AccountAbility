import React from "react";
import { useUser } from "../UserContext";

function Account() {
    const { user } = useUser();

    if (!user) {
        return <p>No user logged in. Please log in first.</p>;
    }

    return (
        <div>
            <h1>Welcome, {user.username}!</h1>
        </div>
    );
}

export default Account;