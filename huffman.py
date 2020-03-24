
import sys, heapq
from collections import deque
from itertools import groupby


class TreeNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

# defined compare functions to be able to use them with heapq
    def _is_valid_operand(self, other):
        return hasattr(other, "frequency")

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.frequency == other.frequency

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            return self.frequency < other.frequency    
    
    def __repr__(self):
        if hasattr(self, 'symbol') and hasattr(self, 'frequency'):
            s = f"Node({self.symbol}, {self.frequency})"
        elif hasattr(self, 'symbol'):
            s = f"Node({self.symbol})"
        elif hasattr(self, 'frequency'):
            s = f"Node({self.frequency})"
        else:
            s = '*'

        return s


""" Generates huffman tree
Uses min heap as a helper structure
"""
def huffman(data):
    if data is None or len(data) == 0:
        return None

    # generate tree nodes with symbols and frequencies
    nodes_queue = [TreeNode(symbol, len(list(group))) for symbol, group in groupby(sorted(data))]
    
    # build priority queue - min frequency high priority (min_heap)
    heapq.heapify(nodes_queue)

    while len(nodes_queue) > 1:
        left = heapq.heappop(nodes_queue)
        right = heapq.heappop(nodes_queue)
        parent = TreeNode(None, left.frequency + right.frequency)
        parent.left_child = left
        parent.right_child = right
        heapq.heappush(nodes_queue, parent) 

    return nodes_queue[0]


""" Generates the huffman tree, traverse through it using recursion
and returns hash table (letter -> code). Than runs through hash table and
returns tuple of encoded data as a string and the tree
"""
def huffman_encoding(data):
    root = huffman(data)
    codes = {}
    _huffman_encoding(codes, "", root)
    
    encoded_data = ""
    for c in data:
        encoded_data += codes[c]
    
    return encoded_data, root


""" While traversing attributes are removed to release some space in the tree
Also hash table is generated to avoid traversing through the tree for each letter
encoding
"""
def _huffman_encoding(codes, s, node):
    if node is None:
        return

    delattr(node, 'frequency')

    if node.symbol:
        if len(s) == 0:
            s = "0"
        codes[node.symbol] = s
    else:
        delattr(node, 'symbol')
        _huffman_encoding(codes, s + "0", node.left_child)
        _huffman_encoding(codes, s + "1", node.right_child)


""" Traverses through the tree and decodes the data
Uses input "byte" to determine where to go - to the left or right.
When reaches a letter, adds it to the string and starts from the root
again
"""
def huffman_decoding(data, tree):
    node = tree
    s = ""
    i = -1
    while i < len(data) - 1:
        if hasattr(node, 'symbol'):
            s += node.symbol;
            node = tree

        i += 1
        if data[i] == '0':
            node = node.left_child
        else:
            node = node.right_child

    if hasattr(node, 'symbol'):
        s += node.symbol
        node = tree

    return s


def print_tree(root):
    if root is None:
        return
    
    q = deque()
    level = 0
    visit_order = list()
    q.append((root, level))
    while len(q) > 0:
        node, level = q.popleft()
        
        if node == None:
            visit_order.append( ("<empty>", level))
            continue
        
        visit_order.append( (node, level) )

        if node.left_child is not None:
            q.append((node.left_child, level + 1))
        else:
            q.append((None, level + 1))
        
        if node.right_child is not None:
            q.append((node.right_child, level + 1))
        else:
            q.append((None, level + 1))

    s = "Huffman tree\n"
    previous_level = -1
    for i in range(len(visit_order)):
        node, level = visit_order[i]
        if level == previous_level:
            s += " | " + str(node) 
        else:
            s += "\n" + str(node)
            previous_level = level
    
    print(s)


if __name__ == "__main__":
    codes = {}

# Test 1: in case of empty string, encoded data is "" and Huffman tree root is None
    print('Test 1:')
    a_great_sentence = ""

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print(f"Encoded data is '{encoded_data}'. Huffman tree root is None => {tree is None}\n")

# Test 2:
    print('Test 2:')
    a_great_sentence = "H"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test 3:
    print('Test 3:')
    a_great_sentence = "Hello"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test 4:
    print('Test 4:')
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the encoded data is: {}".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))