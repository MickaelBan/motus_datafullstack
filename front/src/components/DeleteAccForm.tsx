import React from "react";
import { Navigate } from "react-router-dom";
import "./Sign.css"

type FormProps = {
    legend: string,
    route: string,
    method: string,
    isSignup?: boolean,
    isDelete?: boolean,
}

type FormState = {
    willRedirect: boolean
}



export class DeleteAccForm extends React.Component<FormProps, FormState> {

    private _username: string = "";
    private _willBeDisconnected: boolean = false;


    constructor(props: FormProps | Readonly<FormProps>){
        super(props);

        this.state = {
            willRedirect: false
        }
    }

    async handleSubmit(e: Event){

        e.preventDefault();

        const data = new FormData(e.target as HTMLFormElement);

        const dataBody = JSON.stringify(Object.fromEntries(data));
    
        const postHeaders = {
            "Content-Type": "application/json",
        };

        const route = `http://localhost:5000${this.props.route}`

        console.log(route);

        const rawResponse = await fetch(`http://localhost:5000${this.props.route}`, {
            method: this.props.method, 
            headers: postHeaders,
            body: dataBody
        });

        console.log(rawResponse);


        const jsn = await rawResponse.json();
        const statusCode = jsn["code"];

        if (statusCode === "200"){

            if (this.props.isDelete){
                this._username = "invité";
                this._willBeDisconnected = true;

            }
            else{
                const username = document.getElementById("signinUsername") as HTMLInputElement;
                this._username = username.value;
            }            
            this.setState({willRedirect: true})

        }
        else {

            const nickLabel = document.getElementById("nickLabel") as HTMLElement;
            const pwdLabel = document.getElementById("passwordLabel") as HTMLElement;

            nickLabel.style.fontStyle = "italic";
            nickLabel.innerHTML = " Pseudo - Pseudo ou mdp incorrect."
            nickLabel.style.color = "red";

            pwdLabel.style.fontStyle = "italic";
            pwdLabel.innerHTML = "Mot de passe - Pseudo ou mdp incorrect."
            pwdLabel.style.color = "red";      
        }    
    }

    componentDidMount(): void {

        window.addEventListener("submit", e =>{
            this.handleSubmit(e);
        });

        console.log(this.props);
    }



    render() {
        const redir = this.state.willRedirect;

        return(
            redir ? <Navigate to="/" state={{data: this._username, forcesLogout: !this._willBeDisconnected}}/> : 
            <div className="form-style-5">
                <form method={this.props.method} id="signinForm">
                    <fieldset>
                        <legend>{this.props.legend}</legend>
                                <label id="nickLabel">Pseudo<p className="mandatory">*</p></label>
                                <input type="text" name="nickname" id="signinUsername" placeholder="benisdureau"/>
                
                        
                        <label id="passwordLabel">Mot de passe <p className="mandatory">*</p></label>
                        <input type="password" name="password" id="signinPwd" placeholder="Mot de passe"/>

                    </fieldset>
                    <input type="submit" value="Supprimer"/>
                </form>
            </div>
        );
    }
}