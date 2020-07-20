from backend.utils.crypto_hash import crypto_hash

def test_simple_hash():
	assert crypto_hash.crypto_hash('foo') == 'b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b'

def test_hash_order():
	assert crypto_hash.crypto_hash('foo' ,1 ,[2]) == crypto_hash.crypto_hash([2], 1, 'foo')