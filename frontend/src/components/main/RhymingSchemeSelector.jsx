import {Select, MenuItem} from '@mui/material';

const RhymingSchemeSelector = () => {
<Select labelId="demo-simple-select-label"id="demo-simple-select"value={age}label="ABAB"onChange={handleChange}>
    <MenuItem value={"ABAB"}>ABAB</MenuItem>
    <MenuItem value={"AABB"}>AABB</MenuItem>
    <MenuItem value={"BAAB"}>BAAB</MenuItem>
  </Select>
}

export default RhymingSchemeSelector;