import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import Transactions from './Transactions';
import {API_BASE_URL, MILLISECONDS_JS} from '../config';
import {Button} from 'react-bootstrap';
import history from '../history';
const POLL_INTERVAL = 10 * MILLISECONDS_JS

function TransactionPool(){
	const [transactionPool, setTransactionPool] = useState([]);
	const fetchTransactions = () => {
		fetch(`${API_BASE_URL}/transactions`).
		then(response => response.json()).
		then(json =>{setTransactionPool(json);
					console.log(json);
				});
	}

	const mineTransactions = (event) => {
		fetch(`${API_BASE_URL}/blockchain/mine`).
		then(response => {
			alert('Mining was successful');
			history.push('/blockchain');
	});
	};
	useEffect(() =>{
		fetchTransactions();
		const interval = setInterval(fetchTransactions, POLL_INTERVAL);
		//clear the previously set interval so that useEffect hook can create a fresh interval next time. 
		//return a callback to clear the interval
		return () => clearInterval(interval);
	}, []
		);
	return(
			<div className="TransactionPool">
			<Link to ="/"> Home </Link><br/>
    	<Link to ="/conduct-transactions"> Conduct Transactions </Link><br />
    	<Link to ="/blockchain"> Blockchain </Link>
    	<hr />
			<h3> Transaction History </h3>
			{
				transactionPool.map(transactions =>(
						<div key={transactions.id}>
						<hr />
						<Transactions transactions={transactions} />
						</div>
					))
			}
			<hr />
			<Button variant="danger" size="sm" onClick={mineTransactions}>Mine the transactions</Button>
			</div>
		);
}

export default TransactionPool;