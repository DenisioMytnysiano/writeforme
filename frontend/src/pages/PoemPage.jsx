import { Card, Typography, Stack, Avatar } from "@mui/material";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import PoetryService from "../services/poetry.service";
import ResponsiveAppBar from "../components/common/AppBar";
import PoemCard from "../components/main/PoemCard";
import UserService from "../services/user.service";

const PoemPage = () => {

    const {poemId} = useParams();
    const [poem, setPoem] = useState({});
    const [author, setAuthor] = useState("");

    useEffect(() => {
        PoetryService.getPoem(poemId)
            .then(p => {
                setPoem(p)
                UserService.getUser(p.created_by)
                    .then(a => setAuthor(a.name))
            }
       )
    }, [poemId])

    return <Stack spacing={4} alignItems="center">
        <ResponsiveAppBar/>
        {poem && author && <Stack alignItems="center">
            <Typography sx={{fontSize: 30}}>{poem.title}</Typography>
            <Stack sx={{fontSize: 20}} direction="row" alignItems="center" spacing={2}>
                <Typography>Created by</Typography>
                <Typography>{author}</Typography>
                <Avatar alt={author}></Avatar>
            </Stack>
            <PoemCard sx={{fontSize: 20}} poem={poem.text}></PoemCard>
        </Stack>}
    </Stack>
}

export default PoemPage;