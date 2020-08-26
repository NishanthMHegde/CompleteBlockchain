import React, {useEffect, useState} from 'react';

function Joke(){
	const [joke, setJoke] = useState('');
	useEffect(() => {
		//fetch is an asynchronous call and does not block the rest of the JS code below. It also has ability to handle Promise.
		fetch('https://official-joke-api.appspot.com/jokes/random').
		then(response => response.json()).
		then(joke => {
			console.log('joke' , joke);
			setJoke(joke)
		});
		console.log('Fetching the joke!');
		}
	,[]);
	
	//extract the setup and punchline fields from the joke JSON. Use the same JSON key as in the joke JSON.
	const {setup, punchline} = joke;

	return(
		<div>
		<h3>Joke</h3>
		<p>{setup}</p>
		<p><em>{punchline}</em></p>
		</div>
		);
}

export default Joke;