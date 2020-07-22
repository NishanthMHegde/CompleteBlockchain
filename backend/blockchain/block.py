
import time
from backend.utils.crypto_hash import crypto_hash
from backend.utils.hex_to_binary import hex_to_binary
from backend.config import MINE_RATE

GENESIS_BLOCK = {
	'timestamp': 0,
	'hash':0,
	'last_hash':0,
	'difficulty':3,
	'nonce': 'genesis_nonce',
	'data': '0'
}
class Block:
	"""
	Ledger which consists of information pertaining to the transaction data, timestamp,
	hash of the block and the hash of the previous block.
	"""

	def __init__(self, timestamp, hash, last_hash, difficulty, nonce, data):
		self.timestamp = timestamp
		self.hash = hash
		self.last_hash = last_hash
		self.difficulty = difficulty
		self.nonce = nonce
		self.data = data


	def __repr__(self):
		"""
		Create a string representation of the block
		"""
		block_str = "{timestamp:%s,\nhash:%s,\n,last_hash:%s,\ndata:%s,\n,difficulty:%s,\nnonce:%s,\n}" % \
			(self.timestamp, self.hash, self.last_hash, self.data, self.difficulty, self.nonce)

	@staticmethod
	def mine_block(last_block, data):
		"""
		Static method to mine a block
		"""
		last_hash = last_block.hash
		timestamp = time.time_ns()
		nonce = 0
		difficulty = Block.adjust_difficulty(last_block, timestamp)
		#Make the nonce calculation even more challenging by converting SHA-256 hash to binary 
		#start from 3rd character in hexadecimal representation to remove the 0x
		hash = crypto_hash.crypto_hash(timestamp, last_hash, difficulty, nonce, data)
		while hex_to_binary(hash[2:])[0:difficulty] != '0' * difficulty:
			nonce = nonce + 1
			timestamp = time.time_ns()
			difficulty = Block.adjust_difficulty(last_block, timestamp)
			hash = crypto_hash.crypto_hash(timestamp, last_hash, difficulty, nonce, data)
		return Block(timestamp, hash, last_hash, difficulty, nonce, data)

	@staticmethod
	def adjust_difficulty(last_block, new_timestamp):
		"""
		Method to adjust the difficulty level of the mining based on the previous block timestamp and 
		current timestamp.
		"""
		if new_timestamp - last_block.timestamp < MINE_RATE:
			return last_block.difficulty + 1
		if last_block.difficulty - 1 > 0:
			return last_block.difficulty -1 
		return 1

	@staticmethod
	def genesis():
		"""
		Method to create a Genesis Block.
		"""
		return Block(**GENESIS_BLOCK)
