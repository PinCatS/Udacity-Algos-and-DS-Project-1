# LRU_cache implementation explanation

The requirements were:
* get operation of time O(1)
* set operation of time O(1)
* cache has fixed size of 5
* if cache is full, least recent value is removed.
* Since set time complexity should be O(1), remove also should be O(1)

The following data structures were used:
*  Double linked list
*  Dictionary (Hash Map)

Double linked list gives us O(1) insertion to the head or tail. In my code, I selected to insert to the head (prepend) = most recent element.

Double linked list also gives us O(1) removal
in case we alread point to the node in question.

Hash map is used to provide with access of O(1)

Dictionary keys are mapped to the nodes of double linked list.

I store keys with values in the nodes as well because while removing element from tail of the list, I also need to remove the key from the Hash map and I need to know the key of the element.

For debugging purpose, I redefined __repr__ functions.

Summary of complexities:
get operation O(1)
set operation O(1)

space complexity is O(n) but if to look into details, we need to store 2n keys + n values, so roughly we get O(3n)


