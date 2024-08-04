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
  var clusterRadius = 30 + cs * 4;

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
const MapComponent2 = ({ category, caste, std, classes, setAvgRate, mode }) => {
  // Refs for map and popup
  const mapRef = useRef(null);
  const popupRef = useRef(null);

  const [latLong, setLatLong] = useState([]);
  const [clusters, setClusters] = useState([]);
  const [stateClusters, setStateClusters] = useState([]);
  const [cdHeaders, setCdHeaders] = useState([]);
  const [view, setView] = useState("state");

  // Function to extract cluster from CSV data
  const extractCluster = (loc, clusters) => {
    let cs;
    let colName;
    if (std === "") {
      colName = "prim_" + category;
    } else if (std === "1") {
      colName = "upPrim_" + category;
    } else {
      colName = "snr_" + category;
    }

    for (let i = 0; i < clusters.length; i++) {
      const element = clusters[i];
      if (element.Location === loc) {
        cs = element[colName];
        break;
      }
    }
    return cs;
  };

  useEffect(() => {
    const fetchLatlongData = async () => {
      try {
        const response = await axios.get(`/api/latlong?caste=${caste}`);
        return response;
      } catch (error) {
        console.log(error);
      }
    };

    const fetchClusterData = async () => {
      try {
        const response = await axios.get(`/api/cluster?caste=${caste}`);
        return response;
      } catch (error) {
        console.log(error);
      }
    };

    const fetchStateClusterData = async () => {
      try {
        const response = await axios.get(`/api/state_cluster?caste=${caste}`);
        return response;
      } catch (error) {
        console.log(error);
      }
    };

    Promise.all([
      fetchLatlongData(),
      fetchClusterData(),
      fetchStateClusterData(),
    ]).then(([latLongData, clusterData, stateClusterData]) => {
      if (view === "state") {
        // console.log(latLongData.data);
        let temp = [];
        let st_dno = 100;
        while (st_dno <= 105) {
          for (let i = 0; i < latLongData.data.length - 1; i++) {
            if (Math.floor(latLongData.data[i].DNo / 100) === st_dno) {
              // console.log(
              //   latLongData.data[i].DNo,
              //   i,
              //   latLongData.data[i].state_latitude,
              //   latLongData.data[i].state_longitude
              // );

              console.log(latLongData.data[i]);
            }
          }
          console.log("....................................");
          st_dno++;
        }

        setClusters(stateClusterData.data);
      } else if (view === "district") {
        // console.log(latLongData.data);
        // console.log(clusterData.data);

        setLatLong(latLongData.data);
        setClusters(clusterData.data);
      }
      // setStateClusters(stateClusterData);
      // setClusters(clusterData);
    });
  }, [caste, category, std]);

  // console.log(clusters.data);
  // console.log(latLong.data);

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

    let colName;
    if (std === "") {
      colName = "prim_" + category;
    } else if (std === "1") {
      colName = "upPrim_" + category;
    } else {
      colName = "snr_" + category;
    }

    for (let i = 0; i < latLong?.length; i++) {
      const element = latLong[i];

      // const longitude = element[cdHeaders[0]];
      // const latitude = element[cdHeaders[1]];
      let longitude, latitude;

      longitude = element["longitude"];
      latitude = element["latitude"];

      // console.log(latitude, longitude);

      const rateOp = () => {
        return element[colName];
      };

      const feature_obj = {
        geometry: new Point(
          fromLonLat([parseFloat(longitude), parseFloat(latitude)])
        ),
        rate: parseInt(rateOp()),
        loc: element.Location,
        cs: extractCluster(element.Location, clusters) + 1,
      };

      // console.log(feature_obj);

      const feature = new Feature(feature_obj);
      vectorSource.addFeature(feature);
    }

    // Create a source for clustering
    const clusterSource = new Cluster({
      distance: 60 / Math.pow(2, 0.1), // Adjust the cluster distance as needed
      source: vectorSource,
    });

    // Create a vector layer for clusters
    const clusterLayer = new VectorLayer({
      source: clusterSource,
      style: clusterStyle,
    });

    // Add the cluster layer to the map
    map.addLayer(clusterLayer);

    // Update cluster distance based on map zoom level
    map.getView().on("change:resolution", function (evt) {
      const zoomLevel = map.getView().getZoom();
      const newClusterDistance = 70 / Math.pow(2, zoomLevel - 5.5);
      clusterSource.setDistance(newClusterDistance);
    });

    // Define overlay for displaying cluster information
    const overlay = new Overlay({
      element: popupRef.current,
      positioning: "bottom-center",
      offset: [0, -15],
      stopEvent: false,
    });
    map.addOverlay(overlay);

    if (mode === "dark") {
      map.on("postcompose", function (e) {
        document.querySelector("canvas").style.filter = "invert(90%)";
      });
    }
    map.on("pointermove", (e) => {
      const feature = map.forEachFeatureAtPixel(e.pixel, (feature) => feature);

      if (feature) {
        overlay.setPosition(e.coordinate);

        const dropList = feature.getProperties().features;
        let sum = 0;

        dropList.forEach((element) => {
          sum = sum + element.values_.rate;
        });

        var avgRate = sum / dropList.length || 0;
        avgRate = Math.round(avgRate);

        setAvgRate(avgRate);

        if (avgRate !== undefined) {
          popupRef.current.innerHTML = `Dropout Rate: ${avgRate}%`;
        }
      } else {
        overlay.setPosition(undefined);
      }
    });

    // Clean up when component unmounts
    return () => {
      map.setTarget(null);
    };
  }, [category, caste, std, mode, latLong, clusters, stateClusters]);

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
