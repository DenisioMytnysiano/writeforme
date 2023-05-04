import { useEffect, useState } from "react"
import PoetryService from "../services/poetry.service"
import PoetryPagination from "../components/poetry/PoetryPagination";
import PoetryList from "../components/poetry/PoetryList";
import { Stack } from "@mui/material";
import { useLocation } from "react-router-dom";
import ResponsiveAppBar from "../components/common/AppBar";


const PoetryPage = () => {
    const location = useLocation();
    const query = new URLSearchParams(location.search);
    const page = parseInt(query.get('page') || '1', 10);
    const type = query.get("type") || 'all';
    const itemsPerPage = 10;

    const [poems, setPoems] = useState([])
    useEffect(() => {
        PoetryService.getAllPoems(page, itemsPerPage)
            .then(p => setPoems(p))
    }, [page])

    return <Stack spacing={4} alignItems="center">
        <ResponsiveAppBar/>
        <PoetryList poems={poems}/>
        <PoetryPagination type={type}/>
    </Stack>
}

export default PoetryPage;