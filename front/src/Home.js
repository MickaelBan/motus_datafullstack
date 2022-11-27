import './Home.css';

function Home() {
  return (
    <div className="Home">
        <div className='logo'>
            <p>TUSMO by </p>
            <img src="assets/logo.svg"/>        
        </div>

        <div className='btn-wrapper'>
            <div className='btn' id='play-btn'>Inscription</div>
            <div className='btn' id='login-btn'>Connexion</div>
            <div className='btn' id='signin-btn'>Jouer</div>
        </div>
        
    </div>
  );
}

export default Home;
