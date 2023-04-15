import { TextField } from "@mui/material";

const PoemSeedInput = () => {
    return (
        <TextField 
            id="standard-basic"
            label="Poem seed"
            variant="outlined"
            fullWidth="true" 
            defaultValue=""
            InputLabelProps={{ shrink: true }}
          />
    )
}

export default PoemSeedInput;