import React from 'react';
import { Button, Typography } from "@mui/material";
import { Card, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";
import PoetryService from "../../services/poetry.service";
const PoetryListItem = ({poem, withDelete, onPoemDelete}) => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate(`/poems/${poem.id}`)
    }

    const handleDelete = () => {
        PoetryService.deletePoem(poem.id)
            .then(e => onPoemDelete(poem))
    }
    return <Box sx={{ flexDirection: 'row' }}>
        <Card variant="outlined" onClick={handleClick}>
            <Typography height="50px" fontSize={30} lineHeight="50px">{poem.title}</Typography>
        </Card>
        {withDelete && <Button onClick = {handleDelete}>Delete</Button>}
    </Box>
}

export default PoetryListItem;