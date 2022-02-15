class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
