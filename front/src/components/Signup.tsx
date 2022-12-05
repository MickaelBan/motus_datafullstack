import React from "react";
import { Navigate } from "react-router-dom";
import "./Sign.css"
import { ComplexForm } from "./ComplexForm";



class Signup extends React.Component {

    state = {
        willRedirect: false
    }

    


    render(){

        const willRedirect: boolean = this.state.willRedirect;
        
        return(
            <ComplexForm legend="Ton inscription" route="/users/create" method="POST"></ComplexForm>
        );
    }
}



function onWrongPassword(){

}

function checkPassword(pwd: string){
   
    var re = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/;
    return (re.test(pwd));
}

export default Signup;