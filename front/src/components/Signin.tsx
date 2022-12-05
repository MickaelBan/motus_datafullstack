import React from "react";
import { Navigate } from "react-router-dom"
import { SimpleForm } from "./SimpleForm";
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
            <SimpleForm legend="Connexion" route="/users/login" method="POST"></SimpleForm>
        )
    }
}

export default Signin