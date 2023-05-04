import React from 'react';
import { Navigate } from 'react-router-dom';
import AuthService from '../../services/auth.service';

const AuthRoute = ({ children, onAuthenticated, redirectUrl }) => {
    const sholdRedirect = (!AuthService.isAuthenticated() && !onAuthenticated) || (AuthService.isAuthenticated() && onAuthenticated);
    if (sholdRedirect) {
        return <Navigate to={redirectUrl} />;
    }
    return children;
}
export default AuthRoute;