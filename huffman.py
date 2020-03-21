
import heapq
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


def huffman(input):
    # generate tree nodes with symbols and frequencies
    nodes_queue = [TreeNode(symbol, len(list(group))) for symbol, group in groupby(sorted(input))]
    
    # build priority queue - min frequency high priority (min_heap)
    heapq.heapify(nodes_queue)

    while len(nodes_queue) > 1:
        left = heapq.heappop(nodes_queue)
        right = heapq.heappop(nodes_queue)
        print(left, right)
        parent = TreeNode(None, left.frequency + right.frequency)
        parent.left = left
        parent.rigth = right
        heapq.heappush(nodes_queue, parent) 

    return nodes_queue

def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
    print (huffman(a_great_sentence))

"""     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data)) """