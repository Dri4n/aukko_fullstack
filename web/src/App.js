import React from 'react';
import { Bar } from './features/bar/Bar';
import { Books } from './features/books/Books';
import './App.css';

function App() {
  return (
    <div>
      <Bar />
      <div className={'App-body'}>
        <Books />
      </div>
    </div>
  );
}

export default App;
