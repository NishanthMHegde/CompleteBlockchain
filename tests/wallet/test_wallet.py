from backend.wallet.wallet import Wallet 
from backend.wallet.transactions import Transactions
from backend.blockchain.blockchain import Blockchain
from backend.config import STARTING_BALANCE

def test_sign_data():
	wallet = Wallet()
	data = {'foo':'bar'}
	assert wallet.sign(data)

def test_verify_valid_signature():
	wallet = Wallet()
	data = {'foo':'bar'}
	signature = wallet.sign(data)
	assert Wallet.verify(wallet.public_key, data, signature) == True

def test_verify_invalid_signature():
	wallet = Wallet()
	data = {'foo':'bar'}
	signature = wallet.sign(data)
	assert not Wallet.verify(Wallet().public_key, data, signature) == True
	
def test_wallet_starting_balance():
	wallet = Wallet()
	blockchain = Blockchain()
	assert Wallet.calculate_balance(blockchain, wallet.address) == STARTING_BALANCE

def test_wallet_balance_amount():
	wallet = Wallet()
	blockchain = Blockchain()
	amount = 34
	tr1 = Transactions(wallet, 'recp1', amount)
	blockchain.add_block([tr1.to_json()])
	assert Wallet.calculate_balance(blockchain, wallet.address) == STARTING_BALANCE - amount