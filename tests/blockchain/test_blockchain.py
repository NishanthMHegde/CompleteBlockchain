from backend.blockchain.blockchain import Blockchain
from backend.wallet.transactions import Transactions
from backend.wallet.wallet import Wallet
import pytest

@pytest.fixture
def blockchain():
	blockchain = Blockchain()
	for i in range(3):
		miner_wallet = Wallet()
		transaction = Transactions(Wallet(), 'recipient', i)
		reward_transaction = Transactions.transaction_reward(miner_wallet)
		blockchain.add_block([transaction.to_json()])
		return blockchain

def test_blockchain_instance(blockchain):
	assert isinstance(blockchain, Blockchain)

def test_blockchain_add_block():
	blockchain = Blockchain()
	data = "test-data"
	blockchain.add_block(data)
	assert blockchain.chain[-1].data == data

def test_blockchain_valid(blockchain):
	blockchain.is_chain_valid(blockchain.chain)

def test_blockchain_valid_invalidchain(blockchain):
	blockchain.chain[-1].hash = '0xabc'
	with pytest.raises(Exception, match="The proof of work requirement was not met"):
		blockchain.is_chain_valid(blockchain.chain)

def test_blockchain_valid_invalidgenesis(blockchain):
	blockchain.chain[0].hash = '0xabc'
	with pytest.raises(Exception, match="Genesis block was invalid"):
		blockchain.is_chain_valid(blockchain.chain)

def test_replace_chain(blockchain):
	longer_chain = Blockchain()
	longer_chain.add_block('1')
	longer_chain.add_block('2')
	blockchain.replace_chain(longer_chain.chain)

def test_replace_chain_negative_small_chain(blockchain):
	blockchain.add_block('1')
	blockchain.add_block('2')
	smaller_chain = Blockchain()
	with pytest.raises(Exception, match="Chain length is smaller than current chain."):
		blockchain.replace_chain(smaller_chain.chain)

def test_replace_chain_negative_invalid_chain(blockchain):
	invalid_chain = Blockchain()
	invalid_chain.add_block('1')
	invalid_chain.add_block('1')
	invalid_chain.chain[0].hash = "0xabc"
	with pytest.raises(Exception, match="The incoming chain is not valid"):
		blockchain.replace_chain(invalid_chain.chain)

def test_blockchain_valid_transaction(blockchain):
	Blockchain.is_chain_transaction_valid(blockchain.chain)

def test_blockchain_valid_transaction_duplicate_transactions():
	blockchain = Blockchain()
	transaction = Transactions(Wallet(), 'recipient', 100).to_json()
	blockchain.add_block([transaction, transaction])
	with pytest.raises(Exception, match="is not unique"):
		Blockchain.is_chain_transaction_valid(blockchain.chain)

def test_blockchain_valid_transaction_duplicate_rewardss():
	blockchain = Blockchain()
	transaction = Transactions(Wallet(), 'recipient', 100).to_json()
	reward_transaction = Transactions.transaction_reward(Wallet()).to_json()
	blockchain.add_block([transaction, reward_transaction, reward_transaction])
	with pytest.raises(Exception, match="has multiple rewards"):
		Blockchain.is_chain_transaction_valid(blockchain.chain)
