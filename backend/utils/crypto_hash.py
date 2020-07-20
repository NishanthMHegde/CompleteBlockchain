import hashlib
import json

class crypto_hash:

	@staticmethod
	def crypto_hash(*args):
		"""
		Method to hash the incoming data using SHA256
		"""
		#stringify the incoming data using json library
		stringified_data = map(lambda data: json.dumps(data), args)
		#sort the data to preserve the order of arguments in the incoming data 
		sorted_data = sorted(stringified_data)
		#join the string data
		joined_data = ''.join(sorted_data)
		hashed_data = hashlib.sha256(joined_data.encode('utf-8')).hexdigest()
		return hashed_data
