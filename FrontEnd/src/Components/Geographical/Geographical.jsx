import React from "react";
import MapComponent from "./Map/Map";
import "./Geographical.scss";
const Geographical = () => {
  return (
    <div className="geo-container">
      <div className="geo-content">
        <h1 className="pri-head">GEOGRAPHICAL DISTRIBUTION</h1>
        <div className="map-content">
          <div className="top">
            <MapComponent />
          </div>
          {/* <div className="bottom"></div> */}
        </div>
      </div>
    </div>
  );
};

export default Geographical;
