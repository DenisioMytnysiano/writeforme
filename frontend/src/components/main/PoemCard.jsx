import { Card, Typography } from "@mui/material";

const PoemCard = ({ poem }) => {
    return (<Card elevation={0}>
        {poem.split("\n").map((x, i) => <Typography sx = {{fontSize: 25, margin: 2}}key={i}>{x}</Typography>)}
    </Card>)
}

export default PoemCard;