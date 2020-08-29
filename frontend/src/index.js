import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/App';
import Blockchain from './components/Blockchain';
import ConductTransactions from './components/ConductTransactions';
import TransactionPool from './components/TransactionPool';
import {Router, Switch, Route} from 'react-router-dom';
import history from './history';

ReactDOM.render(
  <Router history={history} >
	<Switch>
	<Route path="/" exact component={App} />
	<Route path="/blockchain" component={Blockchain} />
	<Route path="/conduct-transactions" component={ConductTransactions} />
	<Route path="/transactions" component={TransactionPool} />
	</Switch>
	</Router>,
  document.getElementById('root')
);


