import hashlib
from time import gmtime, strftime

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Block:
    def __init__(self, timestamp, data, index, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash()
    
    def _calc_hash(self):
        sha = hashlib.sha256()
        sha_str = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(sha_str.encode('utf-8'))
        return sha.hexdigest()

    def __str__(self):
        width = 15
        s = '=' * width + '\n'
        s += f"  index    : {self.index}\n"
        s += f"  timestamp: {self.timestamp}\n"
        s += f"  data     : {self.data}\n"
        s += f"  hash     : {self.hash}\n"
        s += f"  prev hash: {self.previous_hash}\n"
        s += '=' * width + '\n'
        return s 

class Blockchain:
    def __init__(self):
        self.head = Node(self._build_genesis_block())
        self.tail = self.head
        self.size = 1

    def add(self, data):
        timestamp = strftime("%H:%M %m/%d/%Y", gmtime())
        block = Block(timestamp, data, self.last_block.index + 1, self.last_block.hash)
        node = Node(block)
        node.next = self.head
        self.head = node
        self.size += 1
        
    def get(self, index):
        if index < 0:
            return None

        current_node = self.head
        while current_node is not None:
            if current_node.value.index == index:
                break
            current_node.next = current_node
        
        return current_node.value

    def size(self):
        return self.size
    
    def _build_genesis_block(self):
        index = 0
        timestamp = strftime("%H:%M %m/%d/%Y", gmtime())
        data = "genesis"
        prev_hash = 0
        return Block(timestamp, data, index, prev_hash)
    
    @property
    def last_block(self):
        return self.head.value

    def __str__(self):
        indent = 7
        current_node = self.head
        s = ""
        while current_node is not None:
            s += str(current_node.value)
            if current_node.next is not None:
                s += ' ' * indent + '|\n'
                s += ' ' * indent + 'V\n'
            current_node = current_node.next
        return s

chain = Blockchain()
print(chain)
chain.add('transaction 1')
chain.add('transaction 2')
chain.add('transaction 3')
print(chain)

print(chain.get(3))

