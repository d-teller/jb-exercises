import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('Loading...');
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    // Fetch data from backend API
    axios.get('/api/data')
      .then(response => {
        setApiData(response.data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setApiData({ error: 'Failed to load data from API' });
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Fullstack Application Demo</h1>
        <div className="card">
          <h2>Frontend</h2>
          <p>React application running in container</p>
        </div>
        
        <div className="card">
          <h2>Backend API Data</h2>
          {apiData ? (
            <pre>{JSON.stringify(apiData, null, 2)}</pre>
          ) : (
            <p>Loading data from API...</p>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;