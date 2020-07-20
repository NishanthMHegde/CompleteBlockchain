
import time
from backend.utils.crypto_hash import crypto_hash

GENESIS_BLOCK = {
	'timestamp': 0,
	'hash':0,
	'last_hash':0,
	'data': '0'
}
class Block:
	"""
	Ledger which consists of information pertaining to the transaction data, timestamp,
	hash of the block and the hash of the previous block.
	"""

	def __init__(self, timestamp, hash, last_hash, data):
		self.timestamp = timestamp
		self.hash = hash
		self.last_hash = last_hash
		self.data = data


	def __repr__(self):
		"""
		Create a string representation of the block
		"""
		block_str = "{timestamp:%s,\nhash:%s,\n,last_hash:%s,\ndata:%s,\n}" % \
			(self.timestamp, self.hash, self.last_hash, self.data)

	@staticmethod
	def mine_block(last_block, data):
		"""
		Static method to mine a block
		"""
		last_hash = last_block.hash
		timestamp = time.time_ns()
		hash = crypto_hash.crypto_hash(timestamp, last_hash, data)
		return Block(timestamp, hash, last_hash, data)

	@staticmethod
	def genesis():
		"""
		Method to create a Genesis Block.
		"""
		return Block(**GENESIS_BLOCK)
