
import sys, heapq
from collections import deque
from itertools import groupby


class TreeNode:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left_child = None
        self.right_child = None

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
        return f"Node({self.symbol}, {self.frequency})"


""" Generates huffman tree
Uses min heap as a helper structure
"""
def huffman(data):
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
    print (f"Hash size: {sys.getsizeof(codes)}")
    
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
    current_level = 0
    q.append((root, 0))
    while len(q) > 0:
        node, level = q.popleft()
        
        if level == 0:
            print(node)
            current_level += 1
        elif level == current_level:
            print(node, end=" ")
        else:
            print()
            print(node, end=" ")
            current_level += 1

        if node.left_child is not None:
            q.append((node.left_child, level + 1))
        
        if node.right_child is not None:
            q.append((node.right_child, level + 1))


def tree_size(node):
    if node is None:
        return 0

    return sys.getsizeof(node) + tree_size(node.left_child) + tree_size(node.right_child)


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print (f"Tree size: {tree_size(tree)}")
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))