import React from 'react';
import * as ReactDOM from "react-dom"
import {createRoot} from "react-dom/client"
import './index.css';
import { BrowserRouter } from "react-router-dom"
import App from './components/App';


const container = document.getElementById('root') as HTMLElement;

const root = createRoot(container);

root.render(
    
    <div className='app'>

      <BrowserRouter>
        <App />
      </BrowserRouter>
    </div>  
);


