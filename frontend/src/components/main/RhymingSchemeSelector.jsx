import {TextField,  MenuItem} from '@mui/material';

const RhymingSchemeSelector = () => {
  return (
    <TextField 
      labelId="demo-simple-select-label"
      id="demo-simple-select" 
      value={"ABAB"} 
      label="Rhyme" 
      select
      style={{width: 100}}
    >
      <MenuItem value={"ABAB"}>ABAB</MenuItem>
      <MenuItem value={"AABB"}>AABB</MenuItem>
      <MenuItem value={"BAAB"}>BAAB</MenuItem>
    </TextField>
  )
}

export default RhymingSchemeSelector;