import React from "react";
import { useLocation } from "react-router-dom";
import { SimpleForm } from "./SimpleForm";

type DelProps = {
    username?: string
}

const DeleteAcc = () => {

    const location = useLocation();

    const route = `/users/${location.state.data}`;

    console.log(route);

    return(
        <SimpleForm legend="Supprimer son compte" route={route} method="DELETE" isDelete={true}></SimpleForm>
    );

}



export default DeleteAcc;