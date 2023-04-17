import {Stack, Container, Button} from "@mui/material";
import RhymingSchemeSelector from './RhymingSchemeSelector';
import PoemSeedInput from './PoemSeedInput';

const PoemGenerationForm = () => {
    return (
        <Container style={{ width: "70%" }} >
            <Stack direction="column" justifyContent="center" spacing={2}>
                <Stack direction="row" justifyContent="center" alignItems="stretch" spacing={1}>
                    <RhymingSchemeSelector />
                    <PoemSeedInput />
                </Stack>
                <Button variant="contained" style={{ width: "20%", minWidth: "200px" }}>Generate poetry</Button>
            </Stack>
        </Container >
    )
}

export default PoemGenerationForm;
