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
  const features = feature.get("features");
  let cs = 2;
  features.forEach((feature) => {
    let c = feature.get("cs");
    cs = c;
  });

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
  var clusterRadius = 30 + cs * 4;

  return new Style({
    image: new CircleStyle({
      radius: clusterRadius,
      stroke: new Stroke({
        color: "black",
        width: 0.2,
      }),
      fill: new Fill({
        color: fillColor,
      }),
    }),
    text: new Text({
      text: cs?.toString(),
      fill: new Fill({
        color: "#fff",
      }),
    }),
  });
};

const fetchLatLongData = async (caste) => {
  const response = await axios.get(`/api/latlong?caste=${caste}`, {
    timeout: 10000,
  });
  return response.data;
};

const fetchClusterData = async (caste) => {
  const response = await axios.get(
    `/api/formatted_cluster_data?caste=${caste}`,
    { timeout: 10000 }
  );
  return response.data;
};

const MapComponent = ({ category, caste, std, classes, setAvgRate, mode }) => {
  const mapRef = useRef(null);
  const popupRef = useRef(null);
  const mapInstance = useRef(null);

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
    const initMap = async () => {
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

      const vectorSource = new VectorSource();

      try {
        const [latLong, clusters] = await Promise.all([
          fetchLatLongData(caste),
          fetchClusterData(caste),
        ]);

        let colName;
        if (std === "") {
          colName = "prim_" + category;
        } else if (std === "1") {
          colName = "upPrim_" + category;
        } else {
          colName = "snr_" + category;
        }

        for (let i = 0; i < latLong.length; i++) {
          const element = latLong[i];
          const longitude = element.longitude;
          const latitude = element.latitude;

          console.log(latitude, longitude);

          const rateOp = () => {
            return element[colName];
          };

          const feature_obj = {
            geometry: new Point(
              fromLonLat([parseFloat(longitude), parseFloat(latitude)])
            ),
            rate: parseInt(rateOp()),
            loc: element.Location,
            cs: extractCluster(element.Location, clusters),
          };

          const feature = new Feature(feature_obj);
          vectorSource.addFeature(feature);
        }

        const clusterSource = new Cluster({
          distance: 60 / Math.pow(2, 0.1),
          source: vectorSource,
        });

        const clusterLayer = new VectorLayer({
          source: clusterSource,
          style: clusterStyle,
        });

        map.addLayer(clusterLayer);

        map.getView().on("change:resolution", function (evt) {
          const zoomLevel = map.getView().getZoom();
          const newClusterDistance = 70 / Math.pow(2, zoomLevel - 5.5);
          clusterSource.setDistance(newClusterDistance);
        });

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
          const feature = map.forEachFeatureAtPixel(
            e.pixel,
            (feature) => feature
          );

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

        return map;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    initMap();

    return () => {
      if (mapInstance.current) {
        mapInstance.current.setTarget(null);
        mapInstance.current = null;
      }
    };
  }, [category, caste, std, mode]);

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

export default MapComponent;
