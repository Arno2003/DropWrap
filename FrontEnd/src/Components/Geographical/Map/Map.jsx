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
import "./Map.scss";

const MapComponent = () => {
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
    fetch("/in.csv")
      .then((response) => response.text())
      .then((csvData) => {
        // Parse CSV data here and create features
        const rows = csvData.split("\n");
        // console.log(rows);

        // Loop through CSV rows and create features
        for (let i = 1; i < rows.length; i++) {
          const [city, lat, lng, country, iso2, admin_name, population] =
            rows[i].split(",");

          // Create a feature for each city
          const feature = new Feature({
            geometry: new Point(fromLonLat([parseFloat(lng), parseFloat(lat)])),
            city,
            country,
            iso2,
            admin_name,
            population: parseInt(population),
          });

          vectorSource.addFeature(feature);
        }

        // Create a source for clustering
        // Create a cluster source
        const clusterSource = new Cluster({
          distance: 40, // Adjust the cluster distance as needed
          source: vectorSource,
        });

        // Create a vector layer for clusters
        const clusterLayer = new VectorLayer({
          source: clusterSource,
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
          // console.log("TRIGGERED");

          const feature = map.forEachFeatureAtPixel(
            e.pixel,
            (feature) => feature
          );

          if (feature) {
            overlay.setPosition(e.coordinate);

            const populationList = feature.getProperties().features;
            let sum = 0;

            populationList.forEach((element) => {
              sum = sum + element.values_.population;
            });

            var avgPop = sum / populationList.length || 0;
            avgPop = Math.round(avgPop);
            console.log(avgPop);

            if (avgPop !== undefined) {
              popupRef.current.innerHTML = `Population: ${avgPop}`;
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
  }, []);

  return (
    <div className="map-container">
      <div
        ref={mapRef}
        className="map"
        style={{ width: "100%", height: "100%" }}
      />
      <div ref={popupRef} className="popup" />
    </div>
  );
};

export default MapComponent;
