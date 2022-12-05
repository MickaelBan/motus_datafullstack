import React from "react";
import { useLocation } from "react-router-dom";
import UpdateForm from "./UpdateForm";


const Update = () => {

    const location = useLocation();

    const route = `/users/update/${location.state.data}`;

    console.log(route);

    return(
        <UpdateForm legend="Mettre à jour son compte" route={route} method="PUT"></UpdateForm>
    );

}



export default Update;