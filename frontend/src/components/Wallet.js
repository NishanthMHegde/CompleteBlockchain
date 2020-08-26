import React, {useState, useEffect} from 'react';
import {API_BASE_URL} from '../config';

function Wallet(){

	const [walletInfo, setWalletInfo] = useState('');
	useEffect(() => {
		fetch(`${API_BASE_URL}/wallet/info`).
		then(response => response.json()).
		then(json => setWalletInfo(json));
	}, []);

	const { address, balance } = walletInfo;

	return (
			<div className="WalletInfo">
			<div>Address: {address}</div>
			<div>Balance: {balance} </div>
			</div>
		);
}

export default Wallet;