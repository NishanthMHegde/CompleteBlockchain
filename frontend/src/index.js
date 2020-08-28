import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransactions from './components/ConductTransactions';
import {Router, Switch, Route} from 'react-router-dom';
import {createBrowserHistory} from 'history';

ReactDOM.render(
  <React.StrictMode>
  <Router history={createBrowserHistory()} >
	<Switch>
	<Route path="/" exact component={App} />
	<Route path="/blockchain" exact component={Blockchain} />
	<Route path="/conduct-transactions" exact component={ConductTransactions} />
	</Switch>
	</Router>
  </React.StrictMode>,
  document.getElementById('root')
);


