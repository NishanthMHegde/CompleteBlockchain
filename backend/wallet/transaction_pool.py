class TransactionPool:
	"""
	Will contain the transaction objects related to each transaction_id.
	"""
	def __init__(self):
		self.transaction_map = dict()

	def set_transaction(self, transaction):
		self.transaction_map[transaction.id] = transaction

	def existing_transaction(self, address):
		#check if a transaction object with the given wallet address exists
		for transaction in self.transaction_map.values():
			if transaction.input['address'] == address:
				return transaction
		return None

	def transaction_data(self):
		"""
		Method to get the transaction data present in the transaction pool \
		in the format of list of JSON.
		"""
		transaction_data = list(map(lambda transaction: transaction.to_json(), self.transaction_map.values()))
		return transaction_data

	def clear_transaction(self, blockchain):
		"""
		Method to clear all the trasnactions in the transaction pool which were a \
		part of any of the blocks in the blockchain.
		"""
		for index,block in enumerate(blockchain.chain):
			if index == 0:
				continue
			for transaction in block.data:
				try:
					del self.transaction_map[transaction['id']]
				except KeyError:
					pass


