import { render } from '@testing-library/react';
import React from 'react';
import './Home.css';
import { Link } from "react-router-dom"

class Home extends React.Component {


  render(){
    return (
      <div className="Home">
        <div className='logo'>
            <p>TUSMO by </p>
            <img src="assets/logo.svg"/>        
        </div>

        <div className='btn-wrapper'>
            <div className='btn' id='play-btn'>Inscription</div>
            <div className='btn' id='login-btn'>Connexion</div>
            <div className='btn' id='signin-btn'><Link to="game">Jouer</Link></div>
        </div>
        
    </div>
    )
  }
}
export default Home;
