from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.wallet import Wallet
from backend.wallet.transactions import Transactions
from backend.blockchain.blockchain import Blockchain
import json
import ast

def test_transaction_pool():
	transaction_pool = TransactionPool()
	transaction1 = Transactions(Wallet() , 'recp1', 10)
	transaction_pool.set_transaction(transaction1)
	assert transaction1.id in transaction_pool.transaction_map.keys()

def test_transaction_clear_transaction():
	transaction_pool = TransactionPool()
	transaction1 = Transactions(Wallet() , 'recp1', 10)
	transaction_pool.set_transaction(transaction1)
	blockchain = Blockchain()
	blockchain.add_block([transaction1.to_json()])
	# assert len(blockchain.chain) > 1
	print(transaction_pool.transaction_map)
	transaction_pool.clear_transaction(blockchain)
	assert transaction1.id not in transaction_pool.transaction_map.keys() 
	# for index, block in enumerate(blockchain.chain):
	# 	if index == 0:
	# 		continue
	# 	for tdata in block.data:
	# 		# tdata = ast.literal_eval(tdata)
	# 		assert tdata['id'] == 'str'