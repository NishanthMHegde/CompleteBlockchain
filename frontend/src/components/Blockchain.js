import React, {useState, useEffect} from 'react';
import {Button} from 'react-bootstrap';
import Block from './Block';
import {API_BASE_URL} from '../config';
import {Link} from 'react-router-dom';
const PAGE_RANGE = 3;

function Blockchain(){
	const [blockchainInfo, setBlockchainInfo] = useState([]);
	const [blockchainLength, setBlockchainLength] = useState(0);
	const getBlockchainRange = ({start, end}) => {
		fetch(`${API_BASE_URL}/blockchain/range?start=${start}&end=${end}`).
		then(response => response.json()).
		then(json => setBlockchainInfo(json));
	}
	useEffect(() => {
		getBlockchainRange({start:0, end:PAGE_RANGE});
		fetch(`${API_BASE_URL}/blockchain/length`).
		then(response => response.json()).
		then(json => setBlockchainLength(json));
	}, []);
	const buttonNumbers = [];
	for (let i=0; i<Math.ceil(blockchainLength/PAGE_RANGE); i++){
		buttonNumbers.push(i);
	}
	

	

return(
	<div className="Blockchain">
	<Link to ="/"> Home </Link><br/>
    <Link to ="/conduct-transactions"> Conduct Transactions </Link>
    <hr />
	<h3>BLockchain</h3>
	<div>{blockchainInfo.map(block => <Block key={block.hash} block={block}/>)}</div>
	{
	buttonNumbers.map(number =>{
		const start = number * PAGE_RANGE;
		const end = (number +1) * PAGE_RANGE;
		return (
			<span key={number} onClick={() => getBlockchainRange({start, end})}><Button variant="danger" size="sm">{number+1}</Button></span>
			)
	})
	}
	</div>
	);
}

export default Blockchain;