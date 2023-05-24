import PoetryListItem from './PoetryListItem';
import { List } from '@mui/material';

const PoetryList = ({ poems, withDelete, onPoemDelete }) => {
    const poemElements = poems.map((poem, i) => { return <PoetryListItem key={i} poem={poem} withDelete={withDelete} onPoemDelete={onPoemDelete}/> })
    return <List sx={{ width: "80%" }} margin={5}>
        {poemElements}
    </List>
};

export default PoetryList;
