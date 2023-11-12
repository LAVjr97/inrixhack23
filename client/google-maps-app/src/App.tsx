import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

var coordinates = new Array();

const containerStyle = {
  width: '80%',
  height: '500px',
  margin: '0 auto',
};

const center = {
  lat: 37.7749,
  lng: -122.4194,
};

function App() {
  const [startPosition, setStartPosition] = useState(center);
  const [clickedPositions, setClickedPositions] = useState<google.maps.LatLngLiteral[]>([]);
  const [coordinatesArray, setCoordinatesArray] = useState<{ lat: number; lng: number }[]>([]);


  const handleMapClick = (event: google.maps.MapMouseEvent | google.maps.IconMouseEvent) => {
    if (clickedPositions.length < 2 && event.latLng) {
      const latLng = event.latLng as google.maps.LatLng;
      setClickedPositions(prevPositions => [...prevPositions, { lat: latLng.lat(), lng: latLng.lng() }]);
    }
  };
  
  
  
  const fetchGeoLocation = async (address: string): Promise<{ lat: number; lng: number }> => {
    const response = await fetch(
      `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(address)}&key=${process.env.REACT_APP_GOOGLE_MAPS_API_KEY || ''}`
    );
    

    const data = await response.json();

    if (data.results && data.results.length > 0) {
      const location = data.results[0].geometry.location;
      return { lat: location.lat, lng: location.lng };
    } else {
      throw new Error('Location not found');
    }
  };

  return (
    <div>

      <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY || ''}>
        <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={10} onClick={handleMapClick}>
          {clickedPositions.map((position, index) => (
            <Marker key={index} position={position} label={`Point ${index + 1}`} />
          ))}
          {startPosition && <Marker position={startPosition} label="Start" />}
        </GoogleMap>
      </LoadScript>
      {clickedPositions.length > 0 && (
        <div>
          <h3>Clicked Positions:</h3>
          {clickedPositions.map((position, index) => (
            <div key={index}>
              <p>Point {index + 1}:</p>
              <p>Latitude: {position.lat}</p>
              <p>Longitude: {position.lng}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
