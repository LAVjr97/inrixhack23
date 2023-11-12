import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';

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
  const [textFieldValues, setTextFieldValues] = useState<string[]>(['', '']);
  
  const handleMapClick = (event: google.maps.MapMouseEvent | google.maps.IconMouseEvent) => {
    if (clickedPositions.length < 2 && event.latLng) {
      const latLng = event.latLng as google.maps.LatLng;
      const clickedPosition = { lat: latLng.lat(), lng: latLng.lng() };

      // Update coordinatesArray with the first two clicked positions
      setCoordinatesArray(prevCoordinates => [
        ...(prevCoordinates.length < 2 ? prevCoordinates : prevCoordinates.slice(2)),
        clickedPosition,
      ]);

      setClickedPositions(prevPositions => [...prevPositions, clickedPosition]);

      if (clickedPositions.length === 0) {
        // Set the start position only once when the first point is clicked
        setStartPosition(clickedPosition);
        setTextFieldValues([`${clickedPosition.lat}`, `${clickedPosition.lng}`]);
      } else {
        setTextFieldValues(prevValues => [...prevValues, `${clickedPosition.lat}`, `${clickedPosition.lng}`]);
      }
    }
  };

  const handleSubmit = () => {
    // Process or use the coordinates as needed
    console.log('Submitted Coordinates:', coordinatesArray);
    // You can add further processing or submit the coordinates to a server here
  };

  return (
    <div>
      <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY || ''}>
        <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={10} onClick={handleMapClick}>
          {clickedPositions.map((position, index) => (
            <Marker key={index} position={position} label={`Point ${index + 0.5}`} />
          ))}
          {startPosition && <Marker position={startPosition} label="Start" />}
        </GoogleMap>
      </LoadScript>

      {textFieldValues.map((value, index) => (
        <div key={index}>
          <label></label>
          <input type="text" value={value} readOnly />
        </div>
      ))}

      {clickedPositions.length === 2 && (
        <button onClick={handleSubmit}>Submit</button>
      )}
    </div>
  );
}

export default App;
