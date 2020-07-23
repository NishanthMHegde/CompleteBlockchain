from backend.blockchain.block import Block 
from backend.blockchain.block import GENESIS_BLOCK
from backend.config import MINE_RATE
from backend.utils.hex_to_binary import hex_to_binary
import time
import pytest


@pytest.fixture
def last_block():
	last_block = Block.genesis()
	return last_block

@pytest.fixture
def mined_block(last_block):
	data = "sample_data"
	mined_block = Block.mine_block(last_block, data)
	return mined_block

def test_mine_block(last_block, mined_block):
	assert isinstance(last_block,Block)
	assert isinstance(mined_block,Block)
	#verify the genesis block 
	for key, value in GENESIS_BLOCK.items():
		assert getattr(last_block, key) == value
	data = "sample_data"
	assert mined_block.data == data
	assert mined_block.last_hash == last_block.hash 
	assert hex_to_binary(mined_block.hash[2:])[0:mined_block.difficulty] == '0' * mined_block.difficulty

def test_block_difficulty():
	last_block = Block.mine_block(Block.genesis(), 'sample_data')
	data = "sample_data"
	mined_block = Block.mine_block(last_block, data)
	assert mined_block.difficulty == last_block.difficulty + 1

def test_block_difficulty_with_minerate():
	last_block = Block.mine_block(Block.genesis(), 'sample1')
	time.sleep(MINE_RATE/1000000000)
	mined_block = Block.mine_block(last_block, 'sample2')
	assert mined_block.difficulty == last_block.difficulty - 1

def test_block_valid(last_block, mined_block):
	Block.is_block_valid(last_block, mined_block)

def test_block_valid_wrong_last_hash(last_block, mined_block):
	mined_block.last_hash = 'wrong_last_hash'
	with pytest.raises(Exception, match='The hash of last block did not match'):
		Block.is_block_valid(last_block, mined_block)

def test_block_valid_wrong_pow(last_block, mined_block):
	mined_block.hash = '0xabcd'
	with pytest.raises(Exception, match='The proof of work requirement was not met'):
		Block.is_block_valid(last_block, mined_block)

def test_block_valid_wrong_difficulty(last_block, mined_block):
	jumped_difficulty = 10
	mined_block.difficulty = jumped_difficulty
	mined_block.hash = "0x%sabcd" % ('0' * jumped_difficulty)
	with pytest.raises(Exception, match='The block difficulty was not valid'):
		Block.is_block_valid(last_block, mined_block)

def test_block_valid_wrong_hash(last_block, mined_block):
	mined_block.hash = "0x%sabcd" % ('0' * mined_block.difficulty)
	with pytest.raises(Exception, match='The block hash was not valid'):
		Block.is_block_valid(last_block, mined_block)

