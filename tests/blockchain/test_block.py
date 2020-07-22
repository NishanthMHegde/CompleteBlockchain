from backend.blockchain.block import Block 
from backend.blockchain.block import GENESIS_BLOCK
from backend.config import MINE_RATE
from backend.utils.hex_to_binary import hex_to_binary
import time

def test_mine_block():
	last_block = Block.genesis()
	assert isinstance(last_block,Block)
	data = "sample_data"
	mined_block = Block.mine_block(last_block, data)
	assert isinstance(mined_block,Block)

	#verify the genesis block 
	for key, value in GENESIS_BLOCK.items():
		assert getattr(last_block, key) == value

	assert mined_block.data == data
	assert mined_block.last_hash == last_block.hash 
	assert hex_to_binary(mined_block.hash[2:])[0:mined_block.difficulty] == '0' * mined_block.difficulty

def test_block_difficulty():
	last_block = Block.mine_block(Block.genesis(), 'sample1')
	mined_block = Block.mine_block(last_block, 'sample2')
	assert mined_block.difficulty == last_block.difficulty + 1

def test_block_difficulty_with_minerate():
	last_block = Block.mine_block(Block.genesis(), 'sample1')
	time.sleep(MINE_RATE/1000000000)
	mined_block = Block.mine_block(last_block, 'sample2')
	assert mined_block.difficulty == last_block.difficulty - 1