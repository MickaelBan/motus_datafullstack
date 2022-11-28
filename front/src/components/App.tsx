import { Routes, Route } from "react-router-dom"
import React from "react"
import Home from "./Home"
import Game from "./Game"


class App extends React.Component {
  
    render(){
        return (
            <div className="App">
                <Routes>
                    <Route path="/" element={ <Home/> } />
                    <Route path="game" element={ <Game/> } />
                </Routes>
            </div>
            )
    }
}

export default App