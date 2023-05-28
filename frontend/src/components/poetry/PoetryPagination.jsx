import * as React from 'react';
import { Link, useLocation } from 'react-router-dom';
import Pagination from '@mui/material/Pagination';
import PaginationItem from '@mui/material/PaginationItem';
import PropTypes from "prop-types";

const PoetryPagination = ({type}) => {
  
  const location = useLocation();
  const query = new URLSearchParams(location.search);
  const page = parseInt(query.get('page') || '1', 10);

  return (
    <Pagination
      page={page}
      count={10}
      renderItem={(item) => (
        <PaginationItem
          component={Link}
          to={`/${type==="mine"? "my-poems" : "poems"}?page=${item.page}`}
          {...item}
        />
      )}
    />
  );
}

PoetryPagination.propTypes = {
  type: PropTypes.string
}

export default PoetryPagination;