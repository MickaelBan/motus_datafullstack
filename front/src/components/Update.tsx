import React from "react";
import { useLocation } from "react-router-dom";
import ComplexForm from "./ComplexForm";
import { SimpleForm } from "./SimpleForm";

type DelProps = {
    username?: string
}

const Update = () => {

    const location = useLocation();

    const route = `/users/update/${location.state.data}`;

    console.log(route);

    return(
        <ComplexForm legend="Mettre à jour son compte" route={route} method="PUT"></ComplexForm>
    );

}



export default Update;