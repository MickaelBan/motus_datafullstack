import React from "react";
import Board from "./Board";

/**
 * turn_index: the current game turn of the user
 * letter_index: the position of the next letter awaiting for input within the grid (essentially a matrix)
 * current_word: a representation of the current word typed by the user
 */
type GameState = {
    turn_index: number
    letter_position: number,
    current_user_word: Array<string>
  }


class Game extends React.Component {

    private _word_to_guess: string = "";
    private _word_length: number = 0;
    
    state: GameState = {
        turn_index: 1,
        letter_position: 1,
        current_user_word: Array<string>()
    }

    constructor(props: {} | Readonly<{}>){
        super(props);

        

        this._word_to_guess = "Baobab";
        this._word_length = this._word_to_guess.length;
        console.log(this.state.current_user_word);
    }


    updateUserWord(letter_input: string, id_to_be_modified: number): void{

        let newArray: string[] = this.state.current_user_word;

        //handling the case where the user wanted to delete the last letter of its word
        if (letter_input === '.'){
            newArray[id_to_be_modified%this._word_length -1] = "."
        }
        else {
            newArray[id_to_be_modified%this._word_length] = letter_input;
        }
        this.setState({current_user_word: newArray});
        console.log("Nouveau mot du user: " + this.state.current_user_word.join(''));
    }


    //On suppose que l'implémentation sera de telle sorte à ce que 
    //dès qu'un user appuie sur entrée, c'est pour vérifier un mot complet
    checkAnswer(): void{

        let occMap: Map<string, number> = new Map();

        let user_answer: string = this.state.current_user_word.join('');
        let next_word_to_guess_from: Array<string> = this.state.current_user_word;
        next_word_to_guess_from[0] = this._word_to_guess[0];


        for (let i = 1; i < this._word_length; i++){

            let lastOccPosition = occMap.get(user_answer[i]);
            let positionToSearchFrom = 1

            if (lastOccPosition !== undefined)
                if (i === lastOccPosition)
                    positionToSearchFrom = lastOccPosition;
                else
                    positionToSearchFrom = lastOccPosition + 1;
            
            else
                positionToSearchFrom = 1;
            
                

            let index = this._word_to_guess.indexOf(user_answer[i], positionToSearchFrom);
            //Tant que la lettre apparaît à partir de la position précisée (1 initialement)
            while (index !== -1){
                //cas où la lettre se trouve dans le mot à trouver, mais à une position différente
                if (i !== index){
                    //coloration au niveau HTML
                    let yellow_square_index = this._word_length*(this.state.turn_index - 1) + i;
                    let yellow_square = document.getElementById(yellow_square_index.toString()) as HTMLElement;
                    yellow_square.style.backgroundColor = yellow_square.style.backgroundColor ? yellow_square.style.backgroundColor : "yellow"
                    
                    
                    // //modification de la lettre au niveau HTML
                    // let modified_square_index = this._word_length*(this.state.turn_index) + i
                    // const square: HTMLElement = document.getElementById(modified_square_index.toString()) as HTMLElement;
                    // square.innerHTML = square.innerHTML ? square.innerHTML : '.';
                }
                else {
                    next_word_to_guess_from[i] = this._word_to_guess[index];
                    
                    
                    // //modification de la lettre au niveau HTML
                    // let modified_square_index = this._word_length*(this.state.turn_index) + i
                    // const square: HTMLElement = document.getElementById((modified_square_index).toString()) as HTMLElement;
                    // square.innerHTML = user_answer[i].toUpperCase();

                    //coloration au niveau HTML
                    let red_square_index = this._word_length * (this.state.turn_index-1) + i;
                    let red_square = document.getElementById(red_square_index.toString()) as HTMLElement;
                    red_square.style.backgroundColor = "red";
                }
                occMap.set(user_answer[i], index);

                index = this._word_to_guess.indexOf(user_answer[i], index + 1);

            }
            if (occMap.get(user_answer[i]) === undefined){
                next_word_to_guess_from[i] = '.';
            }
        }

        

        if (user_answer === this._word_to_guess){
            //route to victory page
            alert("Bravo");
            return;
        }

        console.log("xd", next_word_to_guess_from);
        // for (let i = 1; i < this._word_length; i++){

        //     let index = this._word_length*(this.state.turn_index) + i;

        //     let square = document.getElementById(index.toString()) as HTMLElement;
        //     console.log(square);
        //     square.innerHTML = next_word_to_guess_from[index%next_word_to_guess_from.length].toUpperCase();
        // }

        let prevWordFirstLetter = document.getElementById((this._word_length * (this.state.turn_index-1)).toString()) as HTMLElement;
        prevWordFirstLetter.style.backgroundColor = "red";

        let nextWordFirstLetter = document.getElementById((this._word_length * (this.state.turn_index)).toString()) as HTMLElement;
        nextWordFirstLetter.innerHTML = this._word_to_guess[0];
        this.setState({letter_position: this.state.letter_position + 1});
        this.setState({turn_index: this.state.turn_index+1});

        
    }

    /**
     * 
     * @param keyPressed
     * @param letter_position 
     */
    modifyLetter(keyPressed: string, letter_position: number): void{

        const square = document.getElementById(letter_position.toString()) as HTMLElement;
        square.innerHTML = keyPressed.toUpperCase();

        //This allows us to use the modifyLetter method to handle the backspace presses
        let magic = keyPressed === '.' ? -1 : 1;
        this.updateUserWord(keyPressed, this.state.letter_position);
        this.setState({letter_position: this.state.letter_position + magic});

    }
    /**
     * This method is used to handle special characters: Enter, and Backspace, 
     * as they allow the user to either validate a word, or delete a letter from it.
     * @param p the speJ'ai réusscial key pressed by the user.
     */
    handleSpecialCharacters(p: string): void{
        if (p === "Enter"){
            if (this.state.letter_position/this.state.turn_index !== this._word_length)
                console.log("Mot incomplet");    
            else {
                this.checkAnswer();
            }
        }

        else if (p === "Backspace"){
            console.log("bp")
            if (this.state.letter_position > 1 + this._word_length * (this.state.turn_index - 1)){
                
                this.modifyLetter('.', this.state.letter_position -1)

            }
        }
    
    }

    //Method used to handle keyboard inputs
    handleKeyboardInput(event: KeyboardEvent): void{

        let p = event.key;

        if (this.state.letter_position%this._word_length !== 0){

            console.log(p);

            let regexp = /^[a-zA-Z]+$/

            let a = regexp.test(p);
        
            if (a && p.length < 2){
                this.modifyLetter(p, this.state.letter_position);
            }
        }
        this.handleSpecialCharacters(p);
    }


    async componentDidMount(){
        window.addEventListener("keyup", (event) => {
            this.handleKeyboardInput(event);
        });

        let beginning_array = this.state.current_user_word;
        beginning_array.push(this._word_to_guess.charAt(0));
        this.setState({current_user_word: beginning_array});
        console.log(this.state.current_user_word);

        const response = await fetch('localhost:5000/word');
        // const data = await response.json();
        // console.log(data);
    }

    render(){

        return (
            <div>
                <Board word_length={this._word_length} word={this._word_to_guess} />
                <p>{this._word_to_guess}</p>

            </div>
        );
    }
}





export default Game;