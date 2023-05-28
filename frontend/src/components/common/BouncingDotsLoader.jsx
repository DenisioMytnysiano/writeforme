import React from "react";
import './BouncingDotsLoader.css';
import PropTypes from 'prop-types';

const BouncingDotsLoader = ({text}) => {
    return (
        <div style={{display: "flex", flexDirection: "column", alignItems: "center"}}>
            <div className="bouncing-loader">
                <div></div>
                <div></div>
                <div></div>
            </div>
            <div style={{color: "#a3a1a1"}}>{text}</div>
        </div>
    )
};

BouncingDotsLoader.propTypes = {
    text: PropTypes.string
}

export default BouncingDotsLoader;