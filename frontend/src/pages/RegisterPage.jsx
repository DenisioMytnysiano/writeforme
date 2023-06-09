import React from 'react';
import Container from '@mui/material/Container';
import {Link} from 'react-router-dom';
import RegistrationForm from '../components/register/RegistrationForm';

const RegisterPage = () => {
    return (
        <Container component="main" sx={{display: "flex", alignItems:"center", flexDirection:"column"}}>
          <RegistrationForm/>
          <Link to="/login" style={{color: "#a3a1a1", textDecoration: "none"}}>Already have an account? Login</Link>
        </Container>
    );
}

export default RegisterPage;