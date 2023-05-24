import React, { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import AuthService from '../../services/auth.service';
import {useNavigate} from 'react-router-dom';
import validateEmail from '../../utils/email-validator';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = event => {
        event.preventDefault();
        if(validateState()){
            AuthService.login(email, password)
            .then(() => navigate('/home'))
            .catch(err => setError(err.message));
        }
      };

    const validateState = () => {
        return true;
        if(!validateEmail(email)){
            setError("Invalid email value")
            return false;
        }
        if(password.length == 0){
            setError("Password is empty")
            return false;
        }
    }

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: "20%" }}>
            {error ? (<Typography component="h1" variant="h5">{error}</Typography>) : null}
            <Typography component="h1" variant="h5">Login</Typography>
            <Box component="form" noValidate sx={{ mt: 1 }}>
                <TextField margin="normal" required fullWidth id="email" value={email} label="Email Address" name="email" autoComplete="email" autoFocus onChange={(e) => setEmail(e.target.value)}/>
                <TextField margin="normal" required fullWidth name="password" value={password} label="Password" type="password" id="password" autoComplete="current-password" onChange={(e) => setPassword(e.target.value)}/>
                <Button fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} onClick={handleLogin}>Login</Button>
            </Box>
        </Box>
    )
}

export default LoginForm;