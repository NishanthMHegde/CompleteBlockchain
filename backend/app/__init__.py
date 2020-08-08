import os
import random
import requests
from flask import Flask, jsonify, request
from backend.blockchain.blockchain import Blockchain 
from backend.blockchain.block import Block
from backend.pubsub import PubSub 
from backend.wallet.wallet import Wallet
from backend.wallet.transactions import Transactions
from backend.wallet.transaction_pool import TransactionPool

app = Flask(__name__)
blockchain = Blockchain()
wallet = Wallet()
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)

@app.route('/')
def welcome_blockchain():
    return "Welcome to the Blockchain", 200

@app.route('/blockchain')
def get_blockchain():
    return jsonify(blockchain.to_json()), 200

@app.route('/blockchain/mine')
def mine_block():
    #get the transaction data and put it into the data field of add_block
    transaction_data = transaction_pool.transaction_data()
    blockchain.add_block(transaction_data)
    block = blockchain.chain[-1]
    #publish the block throughout the network to the subscribed channel
    pubsub.broadcast_block(block)
    #After everytime a block is mined, we need to clear the transaction pool.
    transaction_pool.clear_transaction(blockchain)
    return block.to_json(), 200

@app.route('/wallet/transaction', methods=['POST'])
def make_transaction():
    transaction_json = request.get_json()
    #check if transaction exists
    transaction = transaction_pool.existing_transaction(wallet.address)
    if transaction:
        transaction.update_transaction(
            wallet,
            transaction_json['recipient'],
            transaction_json['amount'])
    else:
        transaction = Transactions(
        wallet,
        transaction_json['recipient'],
        transaction_json['amount'])

    #broadcast the transaction object
    pubsub.broadcast_transaction(transaction)
    return jsonify(transaction.to_json())

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
