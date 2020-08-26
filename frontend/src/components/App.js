import React , {useState} from 'react';
import Joke from './Joke';
import Wallet from './Wallet';
import Blockchain from './Blockchain';
import '../App.css';
import logo from '../assets/logo.png';

function App() {
  const [userQuery, setUserQuery] = useState('');
  // const updateUserQuery = (event) => {
  //   console.log('userQuery', userQuery);
  //   setUserQuery(event.target.value);
  // };

  // const searchQuery = (event) => {
  //   window.open(`https://www.google.com/search?q=${userQuery}`);
  // }

  // const enterKeyPress = (event) => {
  //   if (event.key == 'Enter'){
  //     window.open(`https://www.google.com/search?q=${userQuery}`);
  //   };
  // };

  return (
    <div className="App">
    <h3> Welcome to PyChain! </h3>
    <img className="logo" src={logo} alt="application-logo" />  
    <br />
    <Wallet />
    <br />
    <Blockchain />
    </div>
  );
}

export default App;
