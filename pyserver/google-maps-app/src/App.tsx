import React, { useState, useEffect } from 'react';
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

const textFieldContainerStyle: React.CSSProperties = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  position: 'absolute',
  top: '90%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
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

      setCoordinatesArray(prevCoordinates => [
        ...(prevCoordinates.length < 2 ? prevCoordinates : prevCoordinates.slice(2)),
        clickedPosition,
      ]);

      setClickedPositions(prevPositions => [...prevPositions, clickedPosition]);

      if (clickedPositions.length === 0) {
        setStartPosition(clickedPosition);
        setTextFieldValues([`${clickedPosition.lat}`, `${clickedPosition.lng}`]);
      } else {
        setTextFieldValues(prevValues => [...prevValues, `${clickedPosition.lat}`, `${clickedPosition.lng}`]);
      }
    }
  };

  // const handleSubmit = async () => {
  //     const dataToSend = textFieldValues.map(value => parseFloat(value) || 0); // Convert values to numbers
  //     console.log('Data to send:', dataToSend);

  //     // Assuming you have an API endpoint to send data to, adjust the URL accordingly
  //     fetch('https://127.0.0.1:5000/', {
  //       method: 'POST',
  //       headers: {
  //         'Content-Type': 'application/json',
  //       },
  //       body: JSON.stringify(dataToSend),
  //     })
  //     .then(resp => resp.json())
  //     .then(data=> {
  //       console.log("response from backend: ", data)
  //     })
  //     .catch(error=>{console.error("Error sending data: ", error)})
  // }

  const handleSubmit = async () => {
    try {
      const dataToSend = textFieldValues.map(value => parseFloat(value) || 0); // Convert values to numbers
      console.log('Data to send:', dataToSend);
  
      const response = await fetch('https://localhost:5000', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
      });
  
      if (!response.ok) {
        throw new Error(`Failed to submit data: ${response.status} - ${response.statusText}`);
      }
  
      console.log('Data submitted successfully!');
    } catch (error) {
      //console.error('Error submitting data:', error.message);
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

      <div style={textFieldContainerStyle}>
        {textFieldValues.map((value, index) => (
          <div key={index}>
            <label>{`Coordinate ${index + 1}:`}</label>
            <input type="text" value={value} readOnly />
          </div>
        ))}
        {clickedPositions.length === 2 && (
          <button onClick={handleSubmit}>Submit</button>
        )}
      </div>
    </div>
  );
}

export default App;
