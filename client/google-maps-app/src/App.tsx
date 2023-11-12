import React, { useState, useEffect} from 'react'
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

const [startLocation, setStartLocation] = useState('');
const [destinationLocation, setDestinationLocation] = useState('');
const App = () => {
   
    const [clicked, setClicked] = useState(false)

    const handleSubmit = () => {
      console.log('Submitted:', startLocation, destinationLocation);
    };

    return (
      <div></div>
    );
}


const Homepage = () => {
  
  return (<div className="container text-center mt-5">
          <input
            type="text"
            placeholder="Text Field 1"
            className="form-control mb-2"
            value={startLocation}
            onChange={(e) => setStartLocation(e.target.value)}
          />
          <input
            type="text"
            placeholder="Text Field 2"
            className="form-control mb-2"
            value={destinationLocation}
            onChange={(e) => setDestinationLocation(e.target.value)}
          />
          
        </div>
      )
}

const Results = () => {
  const [data, setData] = useState([{}])
    useEffect(() => {
        fetch("/results")
          .then(res=>res.json())
          .then(data => {
          setData(data)
          console.log(data)
        })
    }, [])
  return (
    <LoadScript googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY || ''}>
      <GoogleMap mapContainerStyle={containerStyle} center={center} zoom={12.2}>
        <Marker position={center} />
      </GoogleMap>
    </LoadScript>
  )
}

export default App;
