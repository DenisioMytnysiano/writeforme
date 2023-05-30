import React from "react";
import { Stack, Typography, Button } from "@mui/material";
import ResponsiveAppBar from '../components/common/AppBar';
import PoemGenerationForm from "../components/main/PoemGenerationForm";
import PoemCard from "../components/main/PoemCard";
import { useState } from "react";
import PoetryService from "../services/poetry.service";

const MainPage = () => {

    const [poem, setPoem] = useState("")
    const [saveSuccess, setSaveSuccess] = useState(null);

    const onPoemGenerated = (poem) => {
        setPoem(poem)
        setSaveSuccess(null)
    };

    const onPoemSave = () => {
        PoetryService.save(poem)
            .then(_ => {
                setPoem("")
                setSaveSuccess(true)
            })
            .catch(_ => setSaveSuccess(false))
    };


    return (
        <Stack spacing={4} alignItems="center">
            <ResponsiveAppBar />
            <PoemGenerationForm onPoemGenerated={onPoemGenerated} />
            {poem && (
                <Stack alignItems="center">
                    <Typography textAlign={"center"} fontSize={20}>Your generated poem:</Typography>
                    <PoemCard poem={poem}></PoemCard>
                    <Stack alignContent="center" alignItems="center" direction="row">
                        <Button variant="contained" onClick={onPoemSave}>Save</Button>
                    </Stack>
                </Stack>
            )}
            {saveSuccess != null && (saveSuccess ? <Typography sx={{ backgroundColor: "#90f779", fontSize: 20 }}>Poem saved successfully</Typography> : <Typography sx={{ backgroundColor: "#e8402a", fontSize: 20 }}>Failed to save a poem</Typography>)}
        </Stack>
    )
}

export default MainPage;