from backend.blockchain.blockchain import Blockchain


def test_blockchain_instance():
	blockchain = Blockchain()
	assert isinstance(blockchain, Blockchain)

def test_blockchain_add_block():
	blockchain = Blockchain()
	data = "test-data"
	blockchain.add_block(data)
	assert blockchain.chain[-1].data == data
