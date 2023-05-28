import React from 'react';
import { TextField } from "@mui/material";

const PoemSeedInput = ({onChange}) => {
    return (
        <TextField 
            id="standard-basic"
            label="Poem seed"
            variant="outlined"
            fullWidth="true" 
            defaultValue=""
            InputLabelProps={{ shrink: true }}
            onChange = {(e) => onChange(e.target.value)}
          />
    )
}

export default PoemSeedInput;