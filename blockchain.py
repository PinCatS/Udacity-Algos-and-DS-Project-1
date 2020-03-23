import hashlib
from time import gmtime, strftime

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Block:
    def __init__(self, timestamp, data, index, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash()
    
    def _calc_hash(self):
        sha = hashlib.sha256()
        sha_str = str(self.timestamp) + str(data) + str(previous_hash)
        sha_str.encode('utf-8')
        sha.update(sha_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = Node(self._build_genesys_block())
        self.tail = self.head
        self.size = 1

    def add(self, block):
        pass

    def get(self, index):
        pass

    def size(self):
        return self.size
    
    def _build_genesys_block():
        index = 0
        timestamp = strftime("%H:%M %m/%d/%Y", gmtime())
        data = "genesys"
        prev_hash = 0
        return Block(timestamp, data, index + 1, prev_hash)

