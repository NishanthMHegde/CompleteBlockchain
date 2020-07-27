import uuid
import json
from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

class Wallet:
	"""
	Used to hold the cryptocurrency
	Create signatures using the private key
	Verify signatures using the public key
	"""
	def __init__(self):
		"""
		Initialize the private key, public key, starting balance and the sender's address.
		"""
		self.private_key = ec.generate_private_key(ec.SECP256K1(),
													default_backend())
		self.public_key = self.private_key.public_key() #obtain public key from private key
		self.balance = STARTING_BALANCE
		self.address = str(uuid.uuid4())[:8] #first 8 characters is enough to get 3 trillion different results

	def sign(self, data):
		"""
		Method to sign the string data using the private key using SHA256
		"""
		signature = self.private_key.sign(json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
		return signature

	@staticmethod
	def verify(public_key, data, signature):
		"""
		Method to verify that the signature is valid by using the sender's public key.
		"""
		try:
			public_key.verify(signature, json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
			return True
		except InvalidSignature:
			return False
