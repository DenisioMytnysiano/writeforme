import { Card, Typography, Stack } from "@mui/material";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import PoetryService from "../services/poetry.service";
import ResponsiveAppBar from "../components/common/AppBar";

const PoemPage = () => {

    const {poemId} = useParams();
    const [poem, setPoem] = useState({});

    useEffect(() => {
        PoetryService.getPoem(poemId)
            .then(p => setPoem(p))
    }, [poemId])

    return <Stack spacing={4} alignItems="center">
        <ResponsiveAppBar/>
        {poem && <Card>
            <Typography>{poem.title}</Typography>
            <Typography>{poem.text}</Typography>
        </Card>}
    </Stack>
}

export default PoemPage;