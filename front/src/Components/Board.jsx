import React from "react";
import Square from "./Square";
import "./Board.css"

class Board extends React.Component {
    renderSquare(i ='.') {
      return <Square />;
    }

    componentDidMount(){
      //TODO: handling keypress event listener
      window.addEventListener('keypress', () => {
        alert("ok");
      })
    }
  
    render() {

      return (
        <div>
          <div className="board-row">
            {this.renderSquare("L")}
            {this.renderSquare()}
            {this.renderSquare()}
          </div>
          <div className="board-row">
            {this.renderSquare()}
            {this.renderSquare()}
            {this.renderSquare()}
          </div>
          <div className="board-row">
            {this.renderSquare()}
            {this.renderSquare()}
            {this.renderSquare()}
          </div>
        </div>
      );
    }
  }

export default Board;