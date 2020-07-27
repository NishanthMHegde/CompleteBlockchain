from backend.wallet.transactions import Transactions 
from backend.wallet.wallet import Wallet 
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
