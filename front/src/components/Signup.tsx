import React from "react";
import "./Sign.css"
import { SignupForm } from "./SignupForm";



class Signup extends React.Component {

    state = {
        willRedirect: false
    }

    


    render(){

        const willRedirect: boolean = this.state.willRedirect;
        
        return(
            <SignupForm legend="Ton inscription" route="/users/create" method="POST"></SignupForm>
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