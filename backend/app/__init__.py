import os
import random
import requests
from flask import Flask, jsonify
from backend.blockchain.blockchain import Blockchain 
from backend.blockchain.block import Block
from backend.pubsub import PubSub 

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)

@app.route('/')
def welcome_blockchain():
    return "Welcome to the Blockchain", 200

@app.route('/blockchain')
def get_blockchain():
    return jsonify(blockchain.to_json()), 200

@app.route('/blockchain/mine')
def mine_block():
    blockchain.add_block('sample_data')
    block = blockchain.chain[-1]
    #publish the block throughout the network to the subscribed channel
    pubsub.broadcast_block(block)
    return block.to_json(), 200

ROOT_PORT = 5000
PORT = ROOT_PORT
if os.getenv('PEER'):
    PORT = random.randint(5001, 6000)
    result = requests.get("http://localhost:%s/blockchain" % (ROOT_PORT))
    result_blockchain = Blockchain.from_json(result.json())
    try:
        blockchain.replace_chain(result_blockchain)
        print("Chain replacement with root node was successful")
    except Exception as e:
        print("Chain replacement was not successful: %s" % (e))
app.run(port=PORT)
