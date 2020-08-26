import React , {useState} from 'react';
import Joke from './Joke';
import './App.css';

function App() {
  const [userQuery, setUserQuery] = useState('');
  const updateUserQuery = (event) => {
    console.log('userQuery', userQuery);
    setUserQuery(event.target.value);
  };

  const searchQuery = (event) => {
    window.open(`https://www.google.com/search?q=${userQuery}`);
  }

  const enterKeyPress = (event) => {
    if (event.key == 'Enter'){
      window.open(`https://www.google.com/search?q=${userQuery}`);
    };
  };

  return (
    <div className="App">
    <input value={userQuery} onChange={updateUserQuery} onKeyPress={enterKeyPress}/>
      <button onClick={searchQuery}>Search</button>
      <hr/>
      <Joke/>
    </div>
  );
}

export default App;
