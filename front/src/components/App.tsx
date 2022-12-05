import { Routes, Route } from "react-router-dom"
import React from "react"
import Home from "./Home"
import Game from "./Game"
import Signup from "./Signup"
import Signin from "./Signin"
import DeleteAcc from "./DeleteAcc"
import Update from "./Update"


class App extends React.Component {
  
    render(){
        return (
            <div className="App">
                <Routes>
                    <Route path="/" element={ <Home/> } />
                    <Route path="/game" element={ <Game /> } />
                    <Route path="/signup" element = { <Signup />}/>
                    <Route path="/signin" element = { <Signin />}/>
                    <Route path="/deleteaccount" element = { <DeleteAcc/>}/>
                    <Route path="/update" element = { <Update/>}/>

                </Routes>
            </div>
            )
    }
}

export default App