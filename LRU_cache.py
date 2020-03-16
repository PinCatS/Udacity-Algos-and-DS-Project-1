class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleNode(None)
        self.tail = DoubleNode(None)
        self.head.prev, self.head.next = None, self.tail
        self.tail.prev, self.tail.next = self.head, None
        
        self.num_of_nodes = 0
    
    def append(self, value):
        node = DoubleNode(value)
        prev_to_tail = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev_to_tail
        prev_to_tail.next = node
        
        self.num_of_nodes += 1
        return node        

    def prepend(self, value):
        node = DoubleNode(value)
        next_to_head = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_to_head
        next_to_head.prev = node
        
        self.num_of_nodes += 1
        return node

    def remove(self, node):
        if node == None or self.size() == 0:
            return

        prev_to_node = node.prev
        next_to_node = node.next
        prev_to_node.next = node.next
        next_to_node.prev = node.prev

        self.num_of_nodes -= 1


    def size(self):
        return self.num_of_nodes

    def __repr__(self):
        s = f"Head <->"
        node = self.head.next
        for _ in range(self.num_of_nodes):
            s += f" Node({node.value}) <->"
            node = node.next
        s += f" Tail"

        return s


class LRU_Cache(object):

    def __init__(self, capacity):
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


res = our_cache.get(1)       # returns 1
res = our_cache.get(2)       # returns 2
res = our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

res = our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry