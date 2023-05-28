import React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import AuthService from '../../services/auth.service';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const RegistrationForm = () => {

    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = event => {
        event.preventDefault();
        AuthService.register(name, email, password)
          .then(() => navigate('/home'))
          .catch(err => setError(err.message));
      };

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: "20%" }}>
            {error ? (<Typography component="h1" variant="h5">{error}</Typography>) : null}
            <Typography component="h1" variant="h5">Register</Typography>
            <Box component="form" noValidate sx={{ mt: 1 }}>
                <TextField margin="normal" required fullWidth id="name" value={name} label="Name" name="name" autoComplete="name" autoFocus onChange={e => setName(e.target.value)}/>
                <TextField margin="normal" required fullWidth id="email" value={email} label="Email Address" name="email" autoComplete="email" autoFocus onChange={e => setEmail(e.target.value)}/>
                <TextField margin="normal" required fullWidth name="password" value={password} label="Password" type="password" id="password" autoComplete="current-password" onChange={e => setPassword(e.target.value)}/>
                <Button fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} onClick={handleLogin}>Register</Button>
            </Box>
        </Box>
    )
}

export default RegistrationForm;