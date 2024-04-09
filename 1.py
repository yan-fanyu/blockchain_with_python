import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

class Miner:
    def __init__(self, last_proof):
        self.last_proof = last_proof

    def mine(self):
        proof = 0
        while not self.valid_proof(self.last_proof, proof):
            proof += 1
        return proof

    def valid_proof(self, last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# 创建创世区块
genesis_block = create_genesis_block()
print("Genesis Block has been added to the blockchain!")
print("Hash: %s" % genesis_block.hash)

# 添加新区块
new_block = create_new_block(genesis_block, "New Block Data")
print("New Block has been added to the blockchain!")
print("Index: %s" % new_block.index)
print("Previous Hash: %s" % new_block.previous_hash)
print("Timestamp: %s" % new_block.timestamp)
print("Data: %s" % new_block.data)
print("Hash: %s" % new_block.hash)
