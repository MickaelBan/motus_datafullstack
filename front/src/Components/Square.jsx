import React from 'react';
import "./Board.css"


class Square extends React.Component<{irstLetter}> {
    render() {
      return (
        <button className="square">
          {this.props}
        </button>
      );
    }
}
  
export default Square;
  
  // ========================================