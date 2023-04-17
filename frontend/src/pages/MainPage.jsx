import React from "react";
import {Stack} from "@mui/material";
import ResponsiveAppBar from '../components/common/AppBar';
import PoemGenerationForm from "../components/main/PoemGenerationForm";

const MainPage = () => {
    return (
        <Stack spacing={4} alignItems="center">
            <ResponsiveAppBar/>
            <PoemGenerationForm/>
        </Stack>
    )
}

export default MainPage;