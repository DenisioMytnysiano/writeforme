import { Card, Typography, Stack, Avatar } from "@mui/material";
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
        {poem && <Stack alignItems="center">
            <Typography sx={{fontSize: 30}}>{poem.title}</Typography>
            <Stack sx={{fontSize: 20}} direction="row" alignItems="center" spacing={2}>
                <Typography>Created by</Typography>
                <Typography>Denys Mytnyk</Typography>
                <Avatar alt="Denys Mytnyk"></Avatar>
            </Stack>
            <Typography sx={{fontSize: 20}}>{poem.text}</Typography>
        </Stack>}
    </Stack>
}

export default PoemPage;