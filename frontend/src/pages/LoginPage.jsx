import React from 'react';
import Container from '@mui/material/Container';
import LoginForm from '../components/login/LoginForm';
import {Link} from 'react-router-dom';
const LoginPage = ({email, password}) => {
    return (
        <Container component="main" sx={{display: "flex", alignItems:"center", flexDirection:"column"}}>
          <LoginForm email={email} password={password}/>
          <Link to="/register" style={{color: "#a3a1a1", textDecoration: "none"}}>Don't have an account? Register</Link>
        </Container>
    );
}

export default LoginPage;