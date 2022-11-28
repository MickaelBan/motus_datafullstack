import React from 'react';
import * as ReactDOM from "react-dom"
import './index.css';
import Game from './components/Game';
import { Routes, Route, BrowserRouter as Router, BrowserRouter } from "react-router-dom"
import Home from './components/Home';
import App from './components/App';

ReactDOM.render(
    
    <div className='app'>

      <BrowserRouter>
        <App />
      </BrowserRouter>
    </div>  
   , document.getElementById("root")
);


