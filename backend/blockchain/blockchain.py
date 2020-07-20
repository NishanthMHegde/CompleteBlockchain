from backend.blockchain.block import Block

class Blockchain:
	"""
	Blockchain contains a list of ledgers.
	"""
	def __init__(self):
		self.chain = [Block.genesis()]

	def add_block(self, data):
		"""
		Method to add a block
		"""
		self.chain.append(Block.mine_block(self.chain[-1], data))

	def __repr__(self):
		"""
		String representation of the blockchain.
		"""
		return "Bockchain:%s" % (self.chain)
