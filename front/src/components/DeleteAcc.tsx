import React from "react";
import { useLocation } from "react-router-dom";
import { DeleteAccForm } from "./DeleteAccForm";

type DelProps = {
    username?: string
}

const DeleteAcc = () => {

    const location = useLocation();

    const route = `/users/${location.state.data}`;

    console.log(route);

    return(
        <DeleteAccForm legend="Supprimer son compte" route={route} method="DELETE" isDelete={true}></DeleteAccForm>
    );

}



export default DeleteAcc;