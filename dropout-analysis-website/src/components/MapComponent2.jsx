import React, { useEffect, useRef, useState } from "react";
import "ol/ol.css";
import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile";
import OSM from "ol/source/OSM";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import { Cluster } from "ol/source";
import { Feature } from "ol";
import Point from "ol/geom/Point";
import { fromLonLat } from "ol/proj";
import Overlay from "ol/Overlay";
import { Style, Circle as CircleStyle, Stroke, Fill, Text } from "ol/style";
import axios from "axios";

// Function to define custom style for clusters
const clusterStyle = (feature) => {
  // Retrieve features from the cluster
  const features = feature.get("features");
  // Initialize cluster size
  let cs = 2;
  // Iterate through features to calculate cluster size
  features.forEach((feature) => {
    let c = feature.get("cs");
    cs = c;
  });

  // Define fill color based on cluster size
  let fillColor;
  if (cs == 1) {
    fillColor = "rgba(255, 255, 255, 0.2)";
  } else if (cs == 2) {
    fillColor = "rgba(255, 107, 107, 0.27)";
  } else if (cs == 3) {
    fillColor = "rgba(91, 192, 235, 0.24)";
  } else if (cs == 4) {
    fillColor = "rgba(75, 144, 51, 0.20)";
  } else if (cs == 5) {
    fillColor = "rgba(181, 161, 57, 0.28)";
  } else if (cs == 6) {
    fillColor = "rgba(225, 122, 64, 0.68)";
  } else {
    fillColor = "rgba(225, 64, 64, 0.68)";
  }
  // Adjust the cluster radius based on cluster size
  var clusterRadius = 20 + cs * 5;

  // Return style object for cluster
  return new Style({
    image: new CircleStyle({
      radius: clusterRadius,
      stroke: new Stroke({
        color: "black", // Cluster border color
        width: 0.2, // Cluster border width
      }),
      fill: new Fill({
        color: fillColor, // Cluster fill color based on cluster size
      }),
    }),
    text: new Text({
      text: cs?.toString(),
      fill: new Fill({
        color: "#fff", // Text color
      }),
    }),
  });
};

// MapComponent2 function
const MapComponent2 = ({
  category,
  caste,
  std,
  classes,
  setAvgRate,
  mode,
  stateName,
}) => {
  // Refs for map and popup
  const mapRef = useRef(null);
  const popupRef = useRef(null);

  // Function to extract cluster from CSV data
  const extractCluster = (loc, csvData) => {
    let cs;
    const rows = csvData.split("\n");
    let rows2 = [];
    rows.map((r) => {
      rows2.push(r.split("\r")[0]);
    });

    const headers = rows2[0].split(",");
    let colName;
    if (std === "") {
      colName = category;
    } else {
      colName = category + "." + std;
    }
    const columnIndex = headers.indexOf(colName);
    // Loop through CSV rows and create features
    for (let i = 1; i < rows2.length - 2; i++) {
      const params = rows2[i].split(",");
      if (params[2] !== caste) continue;
      if (params[1] === loc) {
        cs = params[columnIndex];
        break;
      }
    }
    return cs;
  };

  useEffect(() => {
    // Initialize the map
    const map = new Map({
      target: mapRef.current,
      layers: [
        new TileLayer({
          source: new OSM(),
        }),
      ],
      view: new View({
        center: fromLonLat([79.5724, 20.6708]),
        zoom: 5,
      }),
    });
    // Create a vector source for the CSV data
    const vectorSource = new VectorSource();

    axios
      .get(`/api/formatted_cluster_data?dbName=${stateName}`)
      .then((response) => {
        console.log(response.data);
      });

    // Fetch and parse the CSV data
    // fetch("data/latlong.csv")
    //   .then((response) => response.text())
    //   .then((csvData) => {
    //     fetch("data/formatted_cluster_data.csv")
    //       .then((response2) => response2.text())
    //       .then((csvData2) => {
    //         // Parse CSV data here and create features
    //         const rows = csvData.split("\n");

    //         const headers = rows[0].split(",");

    //         let colName;
    //         if (std === "") {
    //           colName = category;
    //         } else {
    //           colName = category + "." + std;
    //         }
    //         const columnIndex = headers.indexOf(colName);

    //         // Loop through CSV rows and create features
    //         for (let i = 1; i < rows.length - 2; i++) {
    //           const params = rows[i].split(",");

    //           const longitude = params[params.length - 1];
    //           const latitude = params[params.length - 2];

    //           if (params[1] !== caste) continue;

    //           const rateOp = () => {
    //             return params[columnIndex];
    //           };

    //           const feature_obj = {
    //             geometry: new Point(
    //               fromLonLat([parseFloat(longitude), parseFloat(latitude)])
    //             ),
    //             rate: parseInt(rateOp()),
    //             loc: params[0],
    //             cs: extractCluster(params[0], csvData2),
    //           };

    //           const feature = new Feature(feature_obj);
    //           vectorSource.addFeature(feature);
    //         }

    //         // Create a source for clustering
    //         const clusterSource = new Cluster({
    //           distance: 60 / Math.pow(2, 6.5 - 8.5), // Adjust the cluster distance as needed
    //           source: vectorSource,
    //         });

    //         // Create a vector layer for clusters
    //         const clusterLayer = new VectorLayer({
    //           source: clusterSource,
    //           style: clusterStyle,
    //         });

    //         // Add the cluster layer to the map
    //         map.addLayer(clusterLayer);

    //         // Update cluster distance based on map zoom level
    //         map.getView().on("change:resolution", function (evt) {
    //           const zoomLevel = map.getView().getZoom();
    //           const newClusterDistance = 60 / Math.pow(2, zoomLevel - 8.5);
    //           clusterSource.setDistance(newClusterDistance);
    //         });

    //         // Define overlay for displaying cluster information
    //         const overlay = new Overlay({
    //           element: popupRef.current,
    //           positioning: "bottom-center",
    //           offset: [0, -15],
    //           stopEvent: false,
    //         });
    //         map.addOverlay(overlay);

    //         if (mode === "dark") {
    //           map.on("postcompose", function (e) {
    //             document.querySelector("canvas").style.filter = "invert(90%)";
    //           });
    //         }
    //         map.on("pointermove", (e) => {
    //           const feature = map.forEachFeatureAtPixel(
    //             e.pixel,
    //             (feature) => feature
    //           );

    //           if (feature) {
    //             overlay.setPosition(e.coordinate);

    //             const dropList = feature.getProperties().features;
    //             let sum = 0;

    //             dropList.forEach((element) => {
    //               sum = sum + element.values_.rate;
    //             });

    //             var avgRate = sum / dropList.length || 0;
    //             avgRate = Math.round(avgRate);

    //             setAvgRate(avgRate);

    //             if (avgRate !== undefined) {
    //               // popupRef.current.innerHTML = `${latitude}, ${longitude}%`;
    //               popupRef.current.innerHTML = `Dropout Rate: ${avgRate}%`;
    //             }
    //           } else {
    //             overlay.setPosition(undefined);
    //           }
    //         });
    //       });
    //   });

    // Clean up when component unmounts
    return () => {
      map.setTarget(null);
    };
  }, [category, caste, std, mode]);

  // setRates(rateArray);

  const handleMouseOut = () => {
    setAvgRate(-1);
  };

  return (
    <div
      className={`h-full border-2 border-dark border-solid z-100 ${classes}`}
    >
      <div
        ref={mapRef}
        className="map z-100 rounded-xl"
        style={{ width: "100%", height: "100%" }}
        onMouseOut={handleMouseOut}
      />
      <div
        ref={popupRef}
        className="bg-light border-2 border-solid border-alt p-6 rounded-5 text-2xl text-dark"
      />
    </div>
  );
};

export default MapComponent2;
