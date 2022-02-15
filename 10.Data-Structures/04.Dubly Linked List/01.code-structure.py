# node blueprint
class Node:
    def __init__(self, val=None):
        self.prev = None
        self.val = val
        self.next = None


# Dubly Linked List
class DublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
