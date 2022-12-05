import React, { useEffect, useState } from 'react';
import './Home.css';
import { Link, useLocation } from "react-router-dom"

const Home = () => {

  const [userName, setUsername] = useState("invité");
  const [isConnected, setConnected] = useState(false);
  
  const location = useLocation();


  useEffect(() => {


    const prevState = location.state;

    if (prevState !== null){
      console.log(prevState);
      setUsername(prevState.data);
      setConnected(prevState.forcesLogout);
      console.log(prevState.forcesLogout)
    }

    window.addEventListener("onclick", () => {

    })

  }, []);

    return (
      <div className="Home">
        <div className='logos'>
            <div className="tusmologo"><img width="509" height="176" src="assets/motus.png"/></div>
            <img src="assets/logo.svg"/>        
        </div>

        <div className='welcome'>
          <p>Bienvenue, {userName}</p>
        </div>

        <div className='btn-wrapper'>
            {!isConnected && <div className='btn' id='play-btn'><Link to="signup">Inscription</Link></div>}
            {!isConnected && <div className='btn' id='login-btn'><Link to="signin">Connexion</Link></div>}
            <div className='btn' id='signin-btn'><Link to="game">Jouer</Link></div>
            {isConnected && 
            <div className="btn" id="modifyPwdBtn">
              <Link to="update" state={{data: userName}}>Modifier compte</Link>
            </div>}


            {isConnected && 
            <div
              className="btn" 
              id="delAccBtn">
                <Link to="deleteaccount" state={{data: userName}} >Supprimer compte</Link>
            </div> }

        </div>
        
    </div>
    )
  }

export default Home;
