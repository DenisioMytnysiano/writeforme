import React from 'react';
import PoetryListItem from './PoetryListItem';
import { List } from '@mui/material';
import PropTypes from 'prop-types';

const PoetryList = ({ poems, withDelete, onPoemDelete }) => {
    const poemElements = poems.map((poem, i) => { return <PoetryListItem key={i} poem={poem} withDelete={withDelete} onPoemDelete={onPoemDelete}/> })
    return <List sx={{ width: "80%" }} margin={5}>
        {poemElements}
    </List>
};

PoetryList.propTypes = {
    poems: PropTypes.array,
    withDelete: PropTypes.bool,
    onPoemDelete: PropTypes.func
}

export default PoetryList;
