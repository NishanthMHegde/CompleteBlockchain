import uuid
import time
from backend.wallet.wallet import Wallet 

class Transactions:
	"""
	Module to handle transactions from the sender to recepient and its amount.
	"""
	def __init__(self, 
				 sender_wallet=None,
				 recipient=None, 
				 amount=None,
				 id=None,
				 output=None,
				 input=None
				 ):
		self.id = id or str(uuid.uuid4())[:8] #create the transaction ID
		#create the transaction going towards recipient
		self.output = output or self.create_output(sender_wallet, recipient, amount)
		#create the transaction part coming back towards the sender
		self.input = input or self.create_input(sender_wallet)

	def create_output(self, sender_wallet, recipient, amount):
		"""
		Create output dictionary
		"""
		if amount > sender_wallet.balance:
			raise Exception("Amount greater than balance")
		output = {}
		output[recipient] = amount
		output[sender_wallet.address] = sender_wallet.balance - amount
		return output

	def create_input(self, sender_wallet):
		"""
		Create input dictionary
		"""
		input = {
		'timestamp': time.time_ns(),
		'address': sender_wallet.address,
		'amount': sender_wallet.balance,
		'public_key': sender_wallet.public_key,
		'signature': sender_wallet.sign(self.output)
		}
		return input

	def update_transaction(self, sender_wallet, recipient, amount):
		"""
		Method to carry out anaother transaction to a recipient.
		"""
		if amount > self.output[sender_wallet.address]:
			raise Exception("Amount greater than balance")
		#check if recipient already exists in the previous transactions by checking the output
		if recipient in self.output:
			self.output[recipient] = self.output[recipient] + amount
		else:
			self.output[recipient] = amount
		self.output[sender_wallet.address] = self.output[sender_wallet.address] - amount
		#create the input transaction dictionary again 
		self.input = self.create_input(sender_wallet)

	@staticmethod
	def verify_transaction(transaction):
		output_total = sum(transaction.output.values())
		#check if sum of all values in output matches the amount in the input dictionary
		if transaction.input['amount'] != output_total:
			raise Exception("Invalid output values")

		#Verify the signature of the transaction
		if not Wallet.verify(transaction.input['public_key'],
							transaction.output,
							transaction.input['signature']
							):
			raise Exception("Invalid Signature")

	def to_json(self):
		"""
		Serialize the transaction object.
		"""
		return self.__dict__

	@staticmethod
	def from_json(transaction_json):
		"""
		De-serialize the transaction object.
		"""
		return Transactions(**transaction_json)



