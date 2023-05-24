import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import AuthService from '../../services/auth.service';
import { useNavigate } from 'react-router-dom';
import { Button } from '@mui/material';


function ResponsiveAppBar() {

  const [anchorElUser, setAnchorElUser] = React.useState(null);
  const navigate = useNavigate();

  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleLoginClick = () => {
    navigate("/login")
  }

  const hangleLogout = () => {
    AuthService.logout()
      .then(e => navigate("/login"))
  }

  const handleAllPoems = () => {
    navigate("/poems/")
  }

  const handleMyPoems = () => {
    navigate("/my-poems/")
  }

  const handleGenerate = () => {
    navigate("/home")
  }

  const settings = [
    {
      name: "Generate",
      onClick: handleGenerate
    },
    {
      name: 'Generated poetry',
      onClick: handleMyPoems
    },
    {
      name: "All poetry",
      onClick: handleAllPoems,
    },
    {
      name: "Logout",
      onClick: hangleLogout
    }];


  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/home"
            sx={{
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            WriteForMe
          </Typography>
          <Typography
            variant="h5"
            noWrap
            component="a"
            href=""
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            WriteForMe
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}></Box>
          {AuthService.isAuthenticated() ?
            (<><Typography sx={{ paddingRight: 1 }}>Denys Mytnyk</Typography><Box sx={{ flexGrow: 0 }}>
              <Tooltip title="Open settings">
                <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                  <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
                </IconButton>
              </Tooltip>
              <Menu
                sx={{ mt: '45px' }}
                id="menu-appbar"
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
              >
                {settings.map((setting) => (
                  <MenuItem key={setting.name} onClick={setting.onClick}>
                    <Typography textAlign="center">{setting.name}</Typography>
                  </MenuItem>
                ))}
              </Menu>
            </Box></>)
            :
            <Button fullWidth variant="text" sx={{ width: 40, height: "100%", color: "white" }} onClick={handleLoginClick}>Login</Button>}
        </Toolbar>
      </Container>
    </AppBar>
  );
}
export default ResponsiveAppBar;