class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # enqueue method
    def enqueue(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    # dequeue method
    def dequeue(self):
        if self.head is None:
            print("queue is empty!")
            return
        else:
            deleteNode = self.head
            self.head = deleteNode.next
            self.length -= 1

            if self.length == 0:
                self.tail = None

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
            return "Queue is empty!"

        return self.head.val

    # tailNode

    def lastNode(self):
        if self.head is None:
            return "Queue is empty!"

        return self.tail.val
    # print

    def Output(self):
        if self.head is None:
            print("Queue is empty!")
        else:
            current = self.head
            while current is not None:
                print(current.val, end="--> ")
                current = current.next
            print("Null")


# initialization
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.dequeue()
print(queue.size())
queue.Output()
