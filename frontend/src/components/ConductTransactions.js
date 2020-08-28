import React, {useState, useEffect} from 'react';
import {Button, FormControl, FormGroup} from 'react-bootstrap';
import {API_BASE_URL} from '../config';
import {Link} from 'react-router-dom';

function ConductTransactions(){
	const [recipient, setReceipient] = useState('');
	const [amount, setAmount] = useState('');

	const onRecipientChange = (event) => {
		setReceipient(event.target.value);
	};
	const onAmountChange = (event) => {
		setAmount(Number(event.target.value));
	};

	const submitTransaction = (event) => {
		fetch(`${API_BASE_URL}/wallet/transaction`,
			{method: 'POST', 
			headers: {'Content-Type': 'application/json'}, 
			body: JSON.stringify({recipient, amount})
		}
	
			).then(response => response.json()).
			then(json =>{
				console.log('Submit Transaction status', json);
				alert('Success!');
			});
		}
	

return (
	<div className="ConductTransaction">
	<Link to ="/"> Home </Link><br/>
    <Link to ="/blockchain"> Blockchain </Link>
    <hr />
	<FormGroup>
	<FormControl 
		input = "text" placeholder="recipient" value={recipient} onChange={onRecipientChange} />
	</FormGroup>
	<FormGroup>
	<FormControl 
		input = "text" placeholder="amount" value={amount} onChange={onAmountChange} />
	</FormGroup>
	<br />
	<Button variant="danger" size="sm" onClick={submitTransaction}>Submit Transaction</Button>
	</div>

	);
}

export default ConductTransactions;