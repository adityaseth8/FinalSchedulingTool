import React from 'react';
import {
  MapContainer,
  TileLayer,
  Marker, 
  Popup
  // Polygon
} from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import MarkerClusterGroup from "react-leaflet-cluster";
import { Icon, divIcon, point } from "leaflet";

// import { statesData } from './data';
import './App.css';

const center = [38.54135231864914, -121.75302174070087];

// markers
const markers = [
  {
    geocode: [38.5413771989718, -121.75309932152891],
    popUp: "California Hall"
  },
  {
    geocode: [38.53956457993359, -121.75473010440209],
    popUp: "Sciences Lecture Building"
  },
  {
    geocode: [38.53798085102295, -121.75568845473931],
    popUp: "Warren and Giedt Hall"
  }
];

// create custom icon
const customIcon = new Icon({
  iconUrl: require('./placeholder.png'),
  iconSize: [40, 40] // size of the icon
});

// custom cluster icon
const createClusterCustomIcon = function (cluster) {
  return new divIcon({
    html: `<span class="cluster-icon">${cluster.getChildCount()}</span>`,
    className: "custom-marker-cluster",
    iconSize: point(33, 33, true)
  });
};

export default function App() {
  return (
    <MapContainer
      center={center}
      zoom={16}
      style={{ width: '100vw', height: '100vh' }}
    >
      <TileLayer
        url="https://api.maptiler.com/maps/basic/256/{z}/{x}/{y}.png?key=xpMKvV4mOW3MWzsnxFP2	"
        attribution='<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
      />
      
      <MarkerClusterGroup
        chunkedLoading
        iconCreateFunction={createClusterCustomIcon}
      >
        {/* Mapping through the markers */}
        {markers.map((marker) => (
          <Marker position={marker.geocode} icon={customIcon}>
            <Popup>{marker.popUp}</Popup>
          </Marker>
        ))}

        {/* Hard coded markers */}
        {/* <Marker position={[51.505, -0.09]} icon={customIcon}>
          <Popup>This is popup 1</Popup>
        </Marker>
        <Marker position={[51.504, -0.1]} icon={customIcon}>
          <Popup>This is popup 2</Popup>
        </Marker>
        <Marker position={[51.5, -0.09]} icon={customIcon}>
          <Popup>This is popup 3</Popup>
        </Marker>
       */}
      </MarkerClusterGroup>
    </MapContainer>
  );
}
