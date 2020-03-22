class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def get_middle(head):
    if head is None:
        return head
    
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


def sortedMerge(left, right):
    if left is None:
        return right

    if right is None:
        return left

    node_left = left
    node_right = right

    new_head = None

    if node_left.value <= node_right.value:
        node = Node(node_left.value)
        new_head = node
        node_left = node_left.next
    else:
        node = Node(node_right.value)
        new_head = node
        node_right = node_right.next
    
    new_tail = new_head

    while node_left is not None and node_right is not None:
        if node_left.value <= node_right.value:
            node = Node(node_left.value)
            node_left = node_left.next
        else:
            node = Node(node_right.value)
            node_right = node_right.next
        
        new_tail.next = node
        new_tail = new_tail.next

    if node_left is None:
        new_tail.next = node_right
    else:
        new_tail.next = node_left
    
    return new_head

def mergeSort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    #split the list into two halves
    middle.next = None

    left = mergeSort(head)
    right = mergeSort(next_to_middle)

    sorted_list_head = sortedMerge(left, right)

    return sorted_list_head

def union(llist_1, llist_2):

    if llist_1.head == None:
        return llist_2
    
    if llist_2.head == None:
        return llist_1

    sorted_list_1_head = mergeSort(llist_1.head)
    sorted_list_2_head = mergeSort(llist_2.head)
    merged_list_head = sortedMerge(sorted_list_1_head, sorted_list_2_head)
    
    node = merged_list_head
    while node.next is not None:
        if node.value == node.next.value:
            current_node = node
            while node.next is not None and node.value == node.next.value:
                node = node.next
            current_node.next = node.next
        node = node.next

    union_list = LinkedList()
    union_list.head = merged_list_head
    return union_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    pass


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

#element_1 = [1, 2, 3]
#element_2 = [2, 3, 6]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print(linked_list_1)
print(linked_list_2)
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))