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

