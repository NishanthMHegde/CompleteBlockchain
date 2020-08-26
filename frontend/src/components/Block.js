import React from 'react';
import {MILLISECONDS} from '../config';
import Transactions from './Transactions';

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
		{
          data.map(transaction => (
            <div key={transaction.id}>
              <hr />
              <Transactions transactions={transaction} />
            </div>
          ))
        }
		</div>
		);
}

export default Block;