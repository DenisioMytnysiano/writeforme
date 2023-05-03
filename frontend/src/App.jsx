import React, { useEffect } from 'react';
import MainPage from './pages/MainPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import PoemPage from './pages/PoemPage';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import AuthRoute from './components/common/AuthRoute';
import AuthService from './services/auth.service';
function App() {

  useEffect(() => {
    AuthService.refreshTokens();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/home" element={<AuthRoute onAuthenticated={false} redirectUrl="/login">
          <MainPage />
        </AuthRoute>}>
        </Route>
        <Route exact path="/poem/:poemId" element={<PoemPage />} />
        <Route exact path="/register" element={
          <AuthRoute onAuthenticated={true} redirectUrl="/home">
            <RegisterPage />
          </AuthRoute>}>
        </Route>
        <Route exact path="/login" element={<AuthRoute onAuthenticated={true} redirectUrl="/home">
          <LoginPage />
        </AuthRoute>}>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App;
