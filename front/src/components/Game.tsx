import React from "react";
import { Navigate } from "react-router-dom";
import Board from "./Board";

/**
 * turn_index: the current game turn of the user
 * letter_index: the position of the next letter awaiting for input within the grid (essentially a matrix)
 * current_word: a representation of the current word typed by the user
 */
type GameState = {
    turn_index: number
    input_length: number
    gameOver: boolean
  }


class Game extends React.Component<any, GameState> {

    private _word_to_guess: string = "";
    private _word_length: number = 0;
    private _gameOver: boolean = false;
    


    async fetchWord() {
        let response = await fetch('http://localhost:5000/word');

        if (response.status === 200){
            let word = await response.json();
            this._word_to_guess = word["result"].toUpperCase();
            this._word_length = this._word_to_guess.length;
        }
    }

    checkAnswer(): void {

        let acc: string = this._word_to_guess[0];

        let letter_pos = (this.state.turn_index - 1) * this._word_length + 1;

        let threshold = letter_pos - 1 + this._word_length;

        let offset = 0;

        //Stores the last occurrence of a given letter we came across through our research
        const lastOccMap: Map<string, number> = new Map();


        for (let i = letter_pos; i < threshold; i++){
            const square = document.getElementById(i.toString()) as HTMLElement;
            const letter = square.innerHTML;


            if (letter === this._word_to_guess[i%this._word_length]){
                square.style.backgroundColor = "red";
                const index = i + this._word_length;

                const el = document.getElementById(index.toString()) as HTMLElement;
                el.innerHTML = letter;
            }
            else {
                const occPos = this._word_to_guess.indexOf(letter, offset);

                if (occPos !== - 1){
                    if (occPos === i%this._word_length){
                
                        //coloration HTML rouge
                        square.style.backgroundColor = "red";
                        const index = i + this._word_length;
    
                        const el = document.getElementById(index.toString()) as HTMLElement;
                        el.innerHTML = letter;
                    }
    
                    else if (occPos !== i%this._word_length){
    
                        let lastOcc = lastOccMap.get(letter);
    
                        //lettre pas encore rencontrée
                        if (lastOcc === undefined){
                            square.style.backgroundColor = "yellow";
                            
                        }
                        else {
                            let lastOccInGuessWord = this._word_to_guess.lastIndexOf(letter);
                            if (lastOccInGuessWord > i%this._word_length){
                                square.style.backgroundColor = "yellow";
                            }
                        }
                    }
                }
                lastOccMap.set(letter, occPos);

            }


            acc+=letter;
        }

        console.log(acc);
        

        console.log(lastOccMap);

        const firstLetterPos = (this.state.turn_index - 1) * this._word_length;

        const firstLetter = document.getElementById(firstLetterPos.toString()) as HTMLElement;
        firstLetter.style.backgroundColor = "red";


        if (acc === this._word_to_guess){
            alert("You have won!");
            this._gameOver = true;
            return;
        }

        offset+=1;

        this.setState({turn_index: this.state.turn_index + 1, input_length: 1})

        if (this.state.turn_index === 6){
            alert("Jeu perdu, le mot à deviner était " + this._word_to_guess);
            this._gameOver = true;
        }

        const firstLetterNextLine = document.getElementById((firstLetterPos + this._word_length).toString()) as HTMLElement;
        firstLetterNextLine.innerHTML = firstLetter.innerHTML;
    }

    
    /**
     * This method is used to handle special characters: Enter, and Backspace, 
     * as they allow the user to either validate a word, or delete a letter from it.
     * @param p the speJ'ai réusscial key pressed by the user.current_user_word:
     */
    handleSpecialCharacters(p: string): void{
        if (p === "Enter"){
            console.log("entree");
            if (this.state.input_length !== this._word_length)
                alert("Mot incomplet");    
            else
               this.checkAnswer();
        }
        else if (p === "Backspace"){
            if (this.state.input_length > 1){
                
                this.modifyLetter('.', (this.state.turn_index - 1) * this._word_length + this.state.input_length - 1);
                this.setState({input_length: this.state.input_length - 1});
            }
        }
    
    }

    /**
     * 
     * @param keyPressed
     * @param letter_position 
     */
    modifyLetter(keyPressed: string, letter_position: number): void{

        const square = document.getElementById(letter_position.toString()) as HTMLElement;
        square.innerHTML = keyPressed.toUpperCase();
    }
    /**
     * This method is used to handle special characters: Enter, and Backspace, 
     * as they allow the user to either validate a word, or delete a letter from it.
     * @param p the speJ'ai réusscial key pressed by the user.
     */
    

    //Method used to handle keyboard inputs
    handleKeyboardInput(event: KeyboardEvent): void{

        let p = event.key;

        if (this.state.input_length !== this._word_length){

            let regexp = /^[a-zA-Z]+$/
            let a = regexp.test(p);
        
            if (a && p.length < 2){
                this.modifyLetter(p, this.state.input_length + (this.state.turn_index - 1) * this._word_length);
                this.setState({input_length: this.state.input_length + 1})
            }
        }
        this.handleSpecialCharacters(p);
    }


    async componentDidMount(){
        window.addEventListener("keydown", (event) => {
            this.handleKeyboardInput(event);
        });

        console.log("ee")

        await this.fetchWord();
        this.setState({turn_index: 1, input_length: 1})


    }

    render(){


        
        return (
            <div>
                {this._gameOver && <Navigate to="/"/>}
                <Board word_length={this._word_length} word={this._word_to_guess} />
            </div>
        );
    }
}





export default Game;