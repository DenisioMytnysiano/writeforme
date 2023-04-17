import React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';


const LoginForm = ({email, password}) => {
    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginTop: "20%" }}>
            <Typography component="h1" variant="h5">Login</Typography>
            <Box component="form" noValidate sx={{ mt: 1 }}>
                <TextField margin="normal" required fullWidth id="email" value={email} label="Email Address" name="email" autoComplete="email" autoFocus />
                <TextField margin="normal" required fullWidth name="password" value={password} label="Password" type="password" id="password" autoComplete="current-password" />
                <Button fullWidth variant="contained" sx={{ mt: 3, mb: 2 }}>Login</Button>
            </Box>
        </Box>
    )
}

export default LoginForm;