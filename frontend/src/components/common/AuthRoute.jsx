import React from 'react';
import { Navigate } from 'react-router-dom';
import AuthService from '../../services/auth.service';
import PropTypes from 'prop-types';

const AuthRoute = ({ children, onAuthenticated, redirectUrl }) => {
    const sholdRedirect = (!AuthService.isAuthenticated() && !onAuthenticated) || (AuthService.isAuthenticated() && onAuthenticated);
    if (sholdRedirect) {
        return <Navigate to={redirectUrl} />;
    }
    return children;
}

AuthRoute.propTypes = {
    children: PropTypes.array,
    onAuthenticated: PropTypes.func.isRequired,
    redirectUrl: PropTypes.string.isRequired
}

export default AuthRoute;