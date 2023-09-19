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
        center: fromLonLat([77.23, 28.61]), // Centered around Delhi
        zoom: 6, // Adjust the initial zoom level as needed
      }),
    });

    // Create a vector source for the CSV data
    const vectorSource = new VectorSource();

    // Fetch and parse the CSV data
    fetch("path/to/your/csv/file.csv")
      .then((response) => response.text())
      .then((csvData) => {
        // ... (previous parsing logic)

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

        // Add hover interaction
        const overlay = new Overlay({
          element: popupRef.current,
          positioning: "bottom-center",
          offset: [0, -15],
          stopEvent: false,
        });
        map.addOverlay(overlay);

        map.on("pointermove", (e) => {
          const feature = map.forEachFeatureAtPixel(
            e.pixel,
            (feature) => feature
          );

          if (feature) {
            overlay.setPosition(e.coordinate);
            const population = feature.get("population");
            if (population !== undefined) {
              popupRef.current.innerHTML = `Population: ${population}`;
            }
          } else {
            overlay.setPosition(undefined);
          }
        });
      });
  }, []);

  return (
    <div>
      <div
        ref={mapRef}
        className="map"
        style={{ width: "100%", height: "400px" }}
      />
      <div ref={popupRef} className="popup" />
    </div>
  );
};

export default MapComponent;
