from backend.wallet.wallet import Wallet
from backend.wallet.transactions import Transactions
from backend.wallet.transaction_pool import TransactionPool
from backend.blockchain.blockchain import Blockchain 
from backend.blockchain.block import Block
import requests
import time
import json

PORT = 5000
def get_blockchain():
	blockchain = requests.get('http://127.0.0.1:%s/blockchain' % (PORT)).json()
	return blockchain

def mine_block():
	requests.get('http://127.0.0.1:%s/blockchain/mine' % (PORT))

def post_transaction(recipient, amount):
	# json_data=json.dumps({'recipient':recipient, 'amount': amount})
	# print(json_data)
	res = requests.post('http://127.0.0.1:%s/wallet/transaction' %(PORT), json={"recipient": recipient, "amount":amount})
	print(res.status_code)

print("Starting blockchain")
blockchain = get_blockchain()
print(blockchain)
recp1 = Wallet().address
recp2 = Wallet().address
post_transaction(recp1, '101')
time.sleep(1)
post_transaction(recp2, '102')
#post the transactions to the app
time.sleep(1)
#mine the block
mine_block()
#get the blockchain again
print("Final blockchain")
blockchain = get_blockchain()
print(blockchain)

#print the balance of the wallet
print("The wallet information is")
print(requests.get('http://127.0.0.1:%s/wallet/info' % (PORT)).json())
