import React from 'react';
import { TextField } from "@mui/material";
import PropTypes from 'prop-types';

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

PoemSeedInput.propTypes = {
    onChange: PropTypes.func
}

export default PoemSeedInput;