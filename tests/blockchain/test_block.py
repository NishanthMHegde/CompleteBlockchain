from backend.blockchain.block import Block 
from backend.blockchain.block import GENESIS_BLOCK

def test_mine_block():
	last_block = Block.genesis()
	assert isinstance(last_block,Block)
	data = "sample_data"
	mined_block = Block.mine_block(last_block, data)
	assert isinstance(mined_block,Block)

	#verify the genesis block 
	for key, value in GENESIS_BLOCK.items():
		assert getattr(last_block, key) == value
		