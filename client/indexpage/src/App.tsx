// App.tsx
import React, { useState } from 'react';
import './App.css';

const App: React.FC = () => {
  const [textField1, setTextField1] = useState('');
  const [textField2, setTextField2] = useState('');

  const handleSubmit = () => {
    console.log('Submitted:', textField1, textField2);
    setTextField1('');
    setTextField2('');
  };

  return (
    <div className="container text-center mt-5">
      <input
        type="text"
        placeholder="Text Field 1"
        className="form-control mb-2"
        value={textField1}
        onChange={(e) => setTextField1(e.target.value)}
      />
      <input
        type="text"
        placeholder="Text Field 2"
        className="form-control mb-2"
        value={textField2}
        onChange={(e) => setTextField2(e.target.value)}
      />
      <button className="btn btn-primary" onClick={handleSubmit}>
        Submit
      </button>
    </div>
  );
};

export default App;
