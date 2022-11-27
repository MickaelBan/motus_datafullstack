import React from 'react';

type SquareState = {
  currentLetter: string
}

type SquareProps = {
  placeholder: string,
  id: string
}


class Square extends React.Component<SquareProps> {

  state: SquareState = {
    currentLetter: this.props.placeholder
  }

    render() {
      return (
        <button id={this.props.id} className="square">
          {this.state.currentLetter}
        </button>
      );
    }
}
  
export default Square;
  
  // ========================================