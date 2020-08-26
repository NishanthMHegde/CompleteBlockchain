import React, {useState, useEffect} from 'react';
import Block from './Block';
import {API_BASE_URL} from '../config';

function Blockchain(){
	const [blockchainInfo, setBlockchainInfo] = useState([]);
	useEffect(() => {
		fetch(`${API_BASE_URL}/blockchain`).
		then(response => response.json()).
		then(json => setBlockchainInfo(json));
	}, []);


return(
	<div className="Blockchain">
	<div>{blockchainInfo.map(block => <Block key={block.hash} block={block}/>)}</div>
	</div>
	);
}

export default Blockchain;