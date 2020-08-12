"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def delete(self):
        if self.next is not None:
            self.next.prev = self.prev

        if self.prev is not None:
            self.prev.next = self.next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        # Check for empty list
        if len(self) == 0:
            # Set New node to head and tail
            self.head = new_node
            self.tail = new_node
        else:
            # If list is not empty, set next to current head
            new_node.next = self.head
            # Set new node to current head.prev
            self.head.prev = new_node
            # Set new node to head
            self.head = new_node

        self.length +=1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        current = self.head
        # Check if head has a next value
        if current.next is not None:
            # Remove connection between current and head's next value
            current.next.prev = None
            # Set new head to current head's next value
            self.head = current.next
        else:
            # if head.next is none, remove the only node from the list
            self.head = None
            self.tail = None
        # decrement length
        self.length -= 1
        return current.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail.delete()
            self.tail = self.tail.prev

        self.length -= 1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.length -= 1
        self.add_to_head(node.value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.head.next is not None and node is not self.tail:
            if node is self.head:
                self.head = self.head.next
            node.delete()
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Is there anything to delete?
        if self.head is None and self.tail is None:
            # returning blank is returning none
            return
        # Check if there only one node
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        # Check if the node is the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # Check if the node is the tail
        elif node is self.tail:
            self.head = node.prev
            node.delete()
        # If it's in the middle
        else: 
            node.delete()
        # Decrement the length
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # If the list is empty return None
        if self.head is None and self.tail is None:
            return
        # Keep track of the largest value we've seen so far
        max_value = self.head.value
        # Traverse the entirety of the linked list
        current = self.head.next
        while current is not None:
            # If we see a value > the largest value we've seen so far
            if current.value > max_value:
                # update the largest value
                max_value = current.value
            # Update current to point to the next node
            current = current.next
        # return the largest value
        return max_value
