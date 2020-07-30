import uuid
import json
from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.utils import (encode_dss_signature, decode_dss_signature)
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
		#serialize the public key so as to easily convert the transaction class to a JSON
		self.public_key = self.serialize_public_key()
		self.balance = STARTING_BALANCE
		self.address = str(uuid.uuid4())[:8] #first 8 characters is enough to get 3 trillion different results

	def serialize_public_key(self):
		return self.public_key.public_bytes(
			encoding = serialization.Encoding.PEM,
			format = serialization.PublicFormat.SubjectPublicKeyInfo
			).decode('utf-8')

	def sign(self, data):
		"""
		Method to sign the string data using the private key using SHA256
		"""
		signature = self.private_key.sign(json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
		#decode the byte format of string to get a tuple of 2 items
		signature = decode_dss_signature(signature)
		return signature

	@staticmethod
	def verify(public_key, data, signature):
		"""
		Method to verify that the signature is valid by using the sender's public key.
		"""
		#deserialize the public key before verifying the signature
		deserialized_public_key = serialization.load_pem_public_key(public_key.encode('utf-8'), default_backend())
		#encode the signature by getting the tuple of (r,s) and then use the deserialzed public key
		r, s = signature
		try:
			deserialized_public_key.verify(encode_dss_signature(r,s), json.dumps(data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
			return True
		except InvalidSignature:
			return False
