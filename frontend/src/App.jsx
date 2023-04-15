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
        <Route exact path="/home" element={<MainPage/>} />
        <Route exact path="/poem/:poemId" element={<PoemPage/>} />
        <Route exact path="/register" element={<RegisterPage/>} />
        <Route exact path="/login" element={<LoginPage email="11" password="12323"/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App;
