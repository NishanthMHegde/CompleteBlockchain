from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration 
from pubnub.callbacks import SubscribeCallback
from backend.blockchain.block import Block
from backend.wallet.transaction_pool import TransactionPool
from backend.wallet.transactions import Transactions
pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-97b26636-ce45-11ea-b3f2-c27cb65b13f4'
pnconfig.publish_key = 'pub-c-15161881-8829-4356-992a-5aeb9a798fa4'

CHANNELS = {
    'TEST':'TEST',
    'BLOCK': 'BLOCK',
    'TRANSACTIONS': 'TRANSACTIONS'
}

class Listener(SubscribeCallback):
    """
    Override the default listener message method to suit our requirements
    """
    def __init__(self, blockchain, transaction_pool):
        self.blockchain = blockchain
        self.transaction_pool = transaction_pool

    def message(self, pubnub, message_object):
        print('Message channel: %s | Message object: %s' % (message_object.channel, message_object.message))
        #check if a block was received through the BLOCK channel and then add it to the chaina and then perform replace chain
        if message_object.channel == 'BLOCK':
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:]
            #add received block to the chain
            potential_chain.append(block)
            #perform replace_chain operation
            try:
                self.blockchain.replace_chain(potential_chain)
                #After everytime a block is mined, we need to clear the transaction pool.
                self.transaction_pool.clear_transaction(self.blockchain)
                print("Chain replacement was successful")
            except Exception as e:
                print("Chain replacement was not successful: %s" % (e))
        elif message_object.channel == 'TRANSACTIONS':
            transaction = Transactions.from_json(message_object.message)
            self.transaction_pool.set_transaction(transaction)


class PubSub():
    """
    Class to handle publish/subscribe from PubNub.
    Used to communicate between different blockchain peers.
    """

    def __init__(self, blockchain, transaction_pool):
        #initialize the pubnub object
        self.pubnub = PubNub(pnconfig)
        #subscribe to the channels that we need to listen to and receive data
        self.pubnub.subscribe().channels(CHANNELS.values()).execute()
        #add the listener to listen for incoming block data
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, message, channel):
        """
        Method to publish a message via a channel
        """
        self.pubnub.publish().channel(channel).message(message).sync()

    def broadcast_block(self, block):
        """
        Method to broadcast the block in the form of JSON to all peers.
        """
        self.publish(block.to_json(), CHANNELS['BLOCK'])

    def broadcast_transaction(self, transaction):
        """
        Method to broadcast the block in the form of JSON to all peers.
        """
        self.publish(transaction.to_json(), CHANNELS['TRANSACTIONS'])


