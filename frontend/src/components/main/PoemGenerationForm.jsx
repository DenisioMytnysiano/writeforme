import { Stack, Container, Button } from "@mui/material";
import RhymingSchemeSelector from './RhymingSchemeSelector';
import PoemSeedInput from './PoemSeedInput';
import { useState } from "react";
import GenerationService from '../../services/generation.service'
import BouncingDotsLoader from "../common/BouncingDotsLoader";
import { Typography } from "@mui/material";

const PoemGenerationForm = ({onPoemGenerated}) => {
    const [rhymingScheme, setRhymingScheme] = useState()
    const [textPrompt, setTextPrompt] = useState()
    const [isLoading, setIsLoading] = useState(false)

    const generate = (e) => {
        setIsLoading(true)
        GenerationService.generate(rhymingScheme, textPrompt)
            .then(poem => {
                setIsLoading(false);
                onPoemGenerated(poem);
            })
    }

    return (
        <Container style={{ width: "70%" }} >
            <Stack direction="column" justifyContent="center" spacing={2}>
                <Stack direction="row" justifyContent="center" alignItems="stretch" spacing={1}>
                    <RhymingSchemeSelector onChange={setRhymingScheme} />
                    <PoemSeedInput onChange={setTextPrompt} />
                </Stack>
                <Button variant="contained" style={{ width: "20%", minWidth: "200px" }} onClick={(e) => generate(e)}>Generate poetry</Button>
                {isLoading && <BouncingDotsLoader text="Generation in progress" />}
            </Stack>
        </Container >
    )
}

export default PoemGenerationForm;
