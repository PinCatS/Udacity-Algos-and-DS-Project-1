# Huffman coding implementation
There is a beautiful way used to generate a list of tree nodes with symbols and their frequencies in one line on pyhton by using list comprehension with itertoools' groupby function.

To build a Huffman tree I used heapq from collections. That is min heap. To be able to use heapq with TreeNodes, I redefined compare methods in TreeNode class

Time complexity of huffman function that builds the tree is O(nlogn):
* Sorting takes O(nlogn)
* Count frequencies O(n)
* Min heap takes O(logn), where n already a number of unique letters
* While loop itself takes Theta(n)

Space complexity is O(n), where n is a number of unique letters

In huffman_encoding function for encoding I used recursion to traverse the tree. I decided to use Hash Map to be able to code all letters with one traversal of the tree. While traversing, I also remove unnecessary fields from the tree to reduce its size.

Time complexity of huffman_encoding is O(n) because there is one traversal of entire tree.
Also to convert Hash Map into a list of codes there if a loop which takes Theta(n) complexity.

Space complexity is O(n) for Hash Map.

Huffman decoding takes O(nlogm) where n is a length of the encoded message and m is a number of unique letters since for each symbol in encoded message we should go down to the leasf of th tree.

For debugging purposes there are print_tree function.

In case empty string is passed for encoding, the empty encoded message is returned as well as root of the tree is None.
