class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # push method
    def push(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    # pop method
    def pop(self):
        if self.head is None:
            print("stack is empty!")
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.length -= 1
            return current.val

    # size method

    def size(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter

    # isEmty method

    def isEmpty(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter == 0

    # firstElement

    def firstNode(self):
        if self.head is None:
            return "Stack is empty!"

        return self.head.val

    # tailNode

    def lastNode(self):
        if self.head is None:
            return "Stack is empty!"

        return self.tail.val
    # print

    def Output(self):
        if self.head is None:
            print("Stack is empty!")
        else:
            current = self.head
            while current is not None:
                print(current.val, end="--> ")
                current = current.next
            print("Null")


# initialization
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.lastNode())
print(stack.isEmpty())
stack.Output()
