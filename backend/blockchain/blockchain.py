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
		return "Blockchain:%s" % (self.chain)

	def to_json(self):
		"""
		Method to serialize a Blockchain object into a JSON/dictionary format.
		"""
		return list(map(lambda block: block.to_json(),self.chain))

	@staticmethod
	def from_json(blockchain_json):
		"""
		Method to deserialize a Blockchain in the form of a dict into an actual Blockchain object.
		"""
		blockchain = Blockchain()
		blockchain.chain = list(map(lambda block: Block.from_json(block),blockchain_json))

	def replace_chain(self, chain):
		"""
		A blockchain can be replaced if:
		1. Length of the incoming chain is greater than the current chain.
		2. The incoming chain is valid.
		"""
		if len(chain) <= len(self.chain):
			raise Exception("Chain length is smaller than current chain.")
		try:
			Blockchain.is_chain_valid(chain)
		except Exception as e:
			raise Exception("%s" % e)
		self.chain = chain 

	@staticmethod
	def is_chain_valid(chain):
		"""
		A Blockchain is said to be valid if:
		1. The Genesis block is valid.
		2. All the blocks in the blockchain are valid.
		"""
		if chain[0] != Block.genesis():
			raise Exception("Genesis block was invalid")
		for i in range(1, len(chain)):
			last_block = chain[i-1]
			block = chain[i]
			Block.is_block_valid(last_block, block)
