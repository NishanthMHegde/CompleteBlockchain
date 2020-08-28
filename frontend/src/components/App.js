import React , {useState} from 'react';
import Joke from './Joke';
import Wallet from './Wallet';
import {Link} from 'react-router-dom';
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
    <div>
    <Link to ="/blockchain"> Blockchain </Link><br/>
    <Link to ="/conduct-transactions"> Conduct Transactions </Link>
    </div>
    </div>
  );
}

export default App;
