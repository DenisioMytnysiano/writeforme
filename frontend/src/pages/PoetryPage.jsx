import React from 'react';
import { useEffect, useState } from "react"
import PoetryService from "../services/poetry.service"
import PoetryPagination from "../components/poetry/PoetryPagination";
import PoetryList from "../components/poetry/PoetryList";
import { Stack } from "@mui/material";
import { useLocation } from "react-router-dom";
import ResponsiveAppBar from "../components/common/AppBar";


const PoetryPage = ({type}) => {
    const location = useLocation();
    const query = new URLSearchParams(location.search);
    const page = parseInt(query.get('page') || '1', 10);
    const itemsPerPage = 10;

    const [poems, setPoems] = useState([])
    useEffect(() => {
        if(type === "mine"){
            PoetryService.getMyPoems(page, itemsPerPage)
                .then(p => setPoems(p))
        }else{
            PoetryService.getAllPoems(page, itemsPerPage)
                .then(p => setPoems(p))
        }
       
    }, [type, page])


    const onPoemDelete = (poem) => {
        setPoems(poems.filter(x => x.id !== poem.id))
    }

    return <Stack spacing={4} alignItems="center">
        <ResponsiveAppBar/>
        <PoetryList poems={poems} withDelete={type === "mine"} onPoemDelete={onPoemDelete}/>
        <PoetryPagination type={type}/>
    </Stack>
}

export default PoetryPage;