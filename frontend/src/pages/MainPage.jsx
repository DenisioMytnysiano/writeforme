import React from "react";
import {Stack, Container, Button} from "@mui/material";
import RhymingSchemeSelector from '../components/main/RhymingSchemeSelector';
import PoemSeedInput from '../components/main/PoemSeedInput';
import AppBar from '../components/common/AppBar';

const MainPage = () => {
    return (
        <Stack spacing={4} alignItems="center">
            <AppBar/>
            <Container style={{width: "70%"}}>
                <Stack direction="column" justifyContent="center" spacing={2}>
                    <Stack direction="row" justifyContent="center" alignItems="stretch" spacing={1}>
                        <RhymingSchemeSelector />
                        <PoemSeedInput />
                    </Stack>
                    <Button variant="contained" style={{width: "20%", minWidth: "200px"}}>Generate poetry</Button>
                </Stack>
            </Container>
        </Stack>
    )
}

export default MainPage;