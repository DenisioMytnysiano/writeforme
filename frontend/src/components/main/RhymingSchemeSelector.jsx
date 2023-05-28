import React from 'react';
import {TextField,  MenuItem} from '@mui/material';
import PropTypes from 'prop-types';

const RhymingSchemeSelector = ({onChange}) => {
  return (
    <TextField 
      id="demo-simple-select" 
      defaultValue={"ABAB"} 
      label="Rhyme" 
      select
      style={{width: 100}}
      onChange={e => onChange(e.target.value)}
    >
      <MenuItem value={"ABAB"}>ABAB</MenuItem>
      <MenuItem value={"AABB"}>AABB</MenuItem>
      <MenuItem value={"BAAB"}>BAAB</MenuItem>
    </TextField>
  )
}

RhymingSchemeSelector.propTypes = {
  onChange: PropTypes.func
}

export default RhymingSchemeSelector;