import React from "react";
import { SigninForm } from "./SigninForm";
import "./Sign.css"

export class Signin extends React.Component {


    state = {
        willRedirect: false,
        userName: ""
    }
    

    render(): React.ReactNode {

        const willRedirect = this.state.willRedirect;
        const data = this.state;

        return(
            <SigninForm legend="Connexion" route="/users/login" method="POST"></SigninForm>
        )
    }
}

export default Signin