import React, {useState, useEffect} from 'react';
import {Button} from 'react-bootstrap';
import {MILLISECONDS} from '../config';
import Transactions from './Transactions';

//TransactionToggle component will be receiving a prop object from Block component which would be the data JSON inside the block
function TransactionToggle({data}){
	var [toggleDisplay, setToggleDisplay] = useState(false);

	const toggleDisplayHandler = (event) => {
		setToggleDisplay(!toggleDisplay);
	};
	//display the transaction information only when the button Show More is clicked.
	if (toggleDisplay){
		return (
			<div>
		{
          data.map(transaction => (
            <div key={transaction.id}>
              <hr />
              <Transactions transactions={transaction} />
            </div>
          ))
        }
		<Button variant="danger" size="sm" onClick={toggleDisplayHandler}>Show Less</Button>
        </div>
        );
	}
	else {
		return (
		<Button variant="danger" size="sm" onClick={toggleDisplayHandler}>Show More</Button>
		);
	}


}

//Block component will be receiving a prop object from Blockchain component
function Block({block}){
	const {hash, last_hash, timestamp, data} = block;

	//convert the timestamp into a human readable date format
	//The timestamp returned from Python is in nanoseconds but JS requires it in milliseconds 
	//and hence needs to be divided by the MILLISECONDS value.
	const timestampDisplay = new Date(timestamp/MILLISECONDS).toLocaleString();
	//use first 16 characters of the hash
	const hashDisplay = `${hash.toString().substring(0, 15)}...`;  
	const lastHashDisplay = `${last_hash.toString().substring(0, 15)}...`; 
	return(
		
		<div className="Block">
		<div>Date:{timestampDisplay}</div>
		<div>Hash:{hashDisplay}</div>
		<div>Previous Hash:{lastHashDisplay}</div>
		<div><TransactionToggle data={data} /></div>
		</div>
		);
}

export default Block;