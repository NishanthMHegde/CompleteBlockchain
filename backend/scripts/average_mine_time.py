from backend.blockchain.blockchain import Blockchain
from backend.config import SECONDS
import time 

times = list()
blockchain = Blockchain()

for i in range(100):
	print("\n")
	start_time = time.time_ns()
	blockchain.add_block(i)
	end_time = time.time_ns()
	time_to_mine = (end_time - start_time) / SECONDS
	times.append(time_to_mine)
	average_time = sum(times)/len(times)
	print("Block difficulty: %s" % (blockchain.chain[-1].difficulty))
	print("Time to mine the new block: %s" % (time_to_mine))
	print("Average time to mine the block: %s" % (average_time))
	print("\n")