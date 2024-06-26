import hashlib
import json

def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()

# 字典 -> json -> sha256 -> 16进制
def hash_block(block):
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hashlib.sha256(json.dumps(hashable_block, sort_keys=True).encode()).hexdigest()
