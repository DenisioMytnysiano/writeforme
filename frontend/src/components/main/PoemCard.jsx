import React from 'react';
import { Card, Typography } from "@mui/material";
import PropTypes from 'prop-types';

const PoemCard = ({ poem }) => {
    return (<Card elevation={0}>
        {poem && poem.split("\n").map((x, i) => <Typography sx = {{fontSize: 25, margin: 2}}key={i}>{x}</Typography>)}
    </Card>)
}

PoemCard.propTypes = {
    poem: PropTypes.string.isRequired
}

export default PoemCard;