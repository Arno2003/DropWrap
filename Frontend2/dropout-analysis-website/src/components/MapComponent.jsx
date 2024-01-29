import React, { useEffect, useRef } from "react";
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
// import "./Map.scss";
import { Style, Circle as CircleStyle, Stroke, Fill, Text } from "ol/style";

// Custom style function for clusters
// Custom style function for clusters
const clusterStyle = (feature) => {
  const features = feature.get("features");
  const clusterSize = features.length;

  // Calculate the average rate for the cluster
  let sum = 0;
  features.forEach((feature) => {
    sum += feature.get("rate");
  });
  const avgRate = sum / clusterSize || 0;

  // Determine cluster color based on avgRate
  let fillColor;
  if (avgRate < 10) {
    fillColor = "rgba(255, 107, 107, 0.27)";
  } else if (avgRate < 20) {
    fillColor = "rgba(91, 192, 235, 0.24)";
  } else if (avgRate < 30) {
    fillColor = "rgba(75, 144, 51, 0.20)";
  } else if (avgRate < 40) {
    fillColor = "rgba(181, 161, 57, 0.28)";
  } else if (avgRate < 50) {
    fillColor = "rgba(225, 122, 64, 0.68)";
  } else {
    fillColor = "rgba(225, 64, 64, 0.68)";
  }

  // Adjust the cluster radius based on your preference
  const clusterRadius = 20 + clusterSize * 5;

  return new Style({
    image: new CircleStyle({
      radius: clusterRadius,
      stroke: new Stroke({
        color: "black", // Cluster border color
        width: 0.2, // Cluster border width
      }),
      fill: new Fill({
        color: fillColor, // Cluster fill color based on avgRate
      }),
    }),
    text: new Text({
      text: clusterSize.toString(),
      fill: new Fill({
        color: "#fff", // Text color
      }),
    }),
  });
};

const MapComponent = ({ category, caste, std, classes, setRates }) => {
  const mapRef = useRef(null);
  const popupRef = useRef(null);
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
        center: fromLonLat([71.5724, 22.6708]),
        zoom: 7.5,
      }),
    });
    // Create a vector source for the CSV data
    const vectorSource = new VectorSource();

    // Fetch and parse the CSV data
    fetch("data/latlong.csv")
      .then((response) => response.text())
      .then((csvData) => {
        // Parse CSV data here and create features
        const rows = csvData.split("\n");
        // console.log(rows);

        // Loop through CSV rows and create features
        for (let i = 1; i < rows.length; i++) {
          const [
            loc,
            soc_cat,
            girls,
            boys,
            ovl,
            girls_1,
            boys_1,
            ovl_1,
            girls_2,
            boys_2,
            ovl_2,
            latitude,
            longitude,
          ] = rows[i].split(",");

          //   console.log(soc_cat, caste);
          if (soc_cat !== caste) continue;

          const rateOp = () => {
            if (category === "G" && std === 0) return girls;
            if (category === "G" && std === 1) return girls_1;
            if (category === "G" && std === 2) return girls_2;
            if (category === "B" && std === 0) return boys;
            if (category === "B" && std === 1) return boys_1;
            if (category === "B" && std === 2) return boys_2;
            if (category === "O" && std === 0) return ovl;
            if (category === "O" && std === 1) return ovl_1;
            if (category === "O" && std === 2) return ovl_2;
          };

          const feature_obj = {
            geometry: new Point(
              fromLonLat([parseFloat(longitude), parseFloat(latitude)])
            ),
            rate: parseInt(rateOp()),
          };

          const feature = new Feature(feature_obj);
          vectorSource.addFeature(feature);
        }

        // Create a source for clustering
        // Create a cluster source
        const clusterSource = new Cluster({
          distance: 10, // Adjust the cluster distance as needed
          source: vectorSource,
        });

        // Create a vector layer for clusters
        const clusterLayer = new VectorLayer({
          source: clusterSource,
          style: clusterStyle,
        });

        // Add the cluster layer to the map
        map.addLayer(clusterLayer);

        const overlay = new Overlay({
          element: popupRef.current,
          positioning: "bottom-center",
          offset: [0, -15],
          stopEvent: false,
        });
        map.addOverlay(overlay);

        map.on("pointermove", (e) => {
          //console.log("TRIGGERED");

          const feature = map.forEachFeatureAtPixel(
            e.pixel,
            (feature) => feature
          );

          if (feature) {
            overlay.setPosition(e.coordinate);

            // console.log(feature);

            const dropList = feature.getProperties().features;
            let sum = 0;

            // console.log(dropList);

            dropList.forEach((element) => {
              // console.log(element.values_.rate);
              sum = sum + element.values_.rate;
            });

            var avgRate = sum / dropList.length || 0;
            avgRate = Math.round(avgRate);
            // console.log(avgRate);

            if (avgRate !== undefined) {
              popupRef.current.innerHTML = `Dropout Rate: ${avgRate}%`;
            }
          } else {
            overlay.setPosition(undefined);
          }
        });
      });

    // Clean up when component unmounts
    return () => {
      map.setTarget(null);
    };
  }, [category, caste, std]);

  // setRates(rateArray);

  return (
    <div
      className={`h-full border-2 border-dark border-solid z-100 ${classes}`}
    >
      <div
        ref={mapRef}
        className="map z-100"
        style={{ width: "100%", height: "100%" }}
      />
      <div
        ref={popupRef}
        className="bg-light border-2 border-solid border-alt p-6 rounded-5 text-2xl text-dark"
      />
    </div>
  );
};

export default MapComponent;
