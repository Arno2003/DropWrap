import React from "react";
import MapComponent from "./Map/Map";
import "./Geographical.scss";
const Geographical = () => {
  return (
    <div className="geo-container">
      <div className="geo-content">
        <h1 className="pri-head">Geographical Distribution</h1>
        <div className="map-content">
          <div className="left">
            <MapComponent />
          </div>
          <div className="right"></div>
        </div>
      </div>
    </div>
  );
};

export default Geographical;
