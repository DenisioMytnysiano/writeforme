import React from "react";
import './BouncingDotsLoader.css';

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


export default BouncingDotsLoader;