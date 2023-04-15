import React  from 'react';
import MainPage from './pages/MainPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import PoemPage from './pages/PoemPage';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/home" component={MainPage} />
        <Route exact path="/poem/:poemId" component={PoemPage} />
        <Route exact path="/register" component={RegisterPage} />
        <Route exact path="/login" component={LoginPage} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
