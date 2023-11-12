import React from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

const containerStyle = {
  width: '50%',
  height: '550px',
  margin: '0 auto',
};

const center = {
  lat: 37.7749,
  lng: -122.4194,
};

function App() {
  return (
    <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY || ''}>
      <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={12.2}>
        <Marker position={center} />
      </GoogleMap>
    </LoadScript>
  );
}

export default App;
