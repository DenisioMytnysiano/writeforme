import { Typography } from "@mui/material";
import { Card } from "@mui/material";
import { useNavigate } from "react-router-dom";
const PoetryListItem = ({poem}) => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate(`/poems/${poem.id}`)
    }
    return <Card variant="outlined" onClick={handleClick}>
        <Typography height="50px" fontSize={30} lineHeight="50px">{poem.text}</Typography>
    </Card>
}

export default PoetryListItem;