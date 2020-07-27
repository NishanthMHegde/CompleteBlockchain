from backend.wallet.wallet import Wallet 

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
	