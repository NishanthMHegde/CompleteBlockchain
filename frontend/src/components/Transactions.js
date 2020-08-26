import React from 'react';

function Transactions({transactions}){
	const {input, output} = transactions;
	//get a list of all recipients
	const recipients = Object.keys(output);
	return(
		<div className="Transaction">
		<div>Sender:{input.address}</div>
		{
			recipients.map(recp_address => (
			<div key={recp_address}>To:{recp_address} | Sent:{output[recp_address]}</div>
			))
		}
		</div>
		);
}

export default Transactions;