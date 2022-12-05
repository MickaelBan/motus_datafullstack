import React from "react";
import Square from "./Square";
import './Board.css'

interface BoardProps {
  word_length: number
  word: string
}

export class Board extends React.Component<BoardProps> {


    renderSquare(i: string = '.', id: number) {
      return <Square id={id.toString()} placeholder={i}/>;
    }

    componentDidMount(){
      
    }
  
    render() {
      return (

      
        <div className="board">
          {
            Array(6).fill(0).map((el, index) => (
              <div className="board-row">
              {Array(this.props.word_length).fill(0).map((el2, index2) => (
                  index === 0 && index2 === 0 
                  ? this.renderSquare(this.props.word.charAt(0), this.props.word_length*index + index2) 
                  : this.renderSquare('.', this.props.word_length*index + index2)
              ))}
              </div>
            ))
          }
        </div>
      );
    }
  }
  
export default Board;