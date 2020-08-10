from backend.wallet.transactions import Transactions 
from backend.wallet.wallet import Wallet 
from backend.config import MINING_REWARD, MINING_REWARD_INPUT
import pytest

def test_transactions_basic():
	wallet = Wallet()
	Transactions(wallet, 'recp1', 100)

def test_transactions_amt_greater_than_balance():
	wallet = Wallet()
	with pytest.raises(Exception, match="Amount greater than balance"):
		Transactions(wallet, 'recp1', 1001)

def test_update_diff_recp_transactions():
	wallet = Wallet()
	transactions = Transactions(wallet, 'recp1', 100)
	transactions.update_transaction(wallet, 'recp2', 100)

def test_update_same_recp_transactions():
	wallet = Wallet()
	transactions = Transactions(wallet, 'recp1', 100)
	transactions.update_transaction(wallet, 'recp1', 100)

def test_update_same_recp_transactions_invalid():
	wallet = Wallet()
	transactions = Transactions(wallet, 'recp1', 100)
	with pytest.raises(Exception, match="Amount greater than balance"):
		transactions.update_transaction(wallet, 'recp1', 901)

def test_verify_transactions():
	wallet = Wallet()
	transactions = Transactions(wallet, 'recp1', 100)
	Transactions.verify_transaction(transactions)

def test_verify_transactions_output_values_wrong():
	wallet = Wallet()
	transactions = Transactions(wallet, 'recp1', 100)
	transactions.input['amount'] = 78
	with pytest.raises(Exception, match = "Invalid output values"):
		Transactions.verify_transaction(transactions)

def test_verify_transactions_invalid_signature():
	wallet = Wallet()
	transactions = Transactions(wallet, 'recp1', 100)
	transactions.input['signature'] = Wallet().sign(transactions.output)
	with pytest.raises(Exception, match = "Invalid Signature"):
		Transactions.verify_transaction(transactions)

def test_transactions_reward():
	miner_wallet = Wallet()
	reward_transaction = Transactions.transaction_reward(miner_wallet)
	assert reward_transaction.output[miner_wallet.address] == MINING_REWARD
	assert reward_transaction.input == MINING_REWARD_INPUT

def test_transactions_validate_reward():
	miner_wallet = Wallet()
	reward_transaction = Transactions.transaction_reward(miner_wallet)
	Transactions.verify_transaction(reward_transaction)

def test_transactions_validate_invalid_reward():
	miner_wallet = Wallet()
	reward_transaction = Transactions.transaction_reward(miner_wallet)
	reward_transaction.output[miner_wallet.address] = 101
	with pytest.raises(Exception, match="Invalid transaction reward"):
		Transactions.verify_transaction(reward_transaction)

def test_transactions_validate_invalid_rewards():
	miner_wallet = Wallet()
	reward_transaction = Transactions.transaction_reward(miner_wallet)
	reward_transaction.output[miner_wallet.address] = 100
	reward_transaction.output['recp1'] = 100
	with pytest.raises(Exception, match="Invalid transaction reward"):
		Transactions.verify_transaction(reward_transaction)