class Queue:
    # constructor
    def __init__(self):
        self.data = []

    # enqueue method
    def enqueue(self, item):
        self.data.append(item)

    # dequeue method
    def dequeue(self):
        if len(self.data):
            return self.data.pop(0)
        else:
            return "dequeue failed!"

    # size method
    def size(self):
        return len(self.data)

    # isEmpty method
    def isEmpty(self):
        return len(self.data) == 0

    # topElement method
    def topElement(self):
        if(len(self.data)):
            return self.data[0]
        else:
            return "queue is empty!"

    # tailElement
    def tailElement(self):
        if(len(self.data)):
            return self.data[-1]
        else:
            return "queue is empty!"


queue = Queue()
queue.enqueue("tori")
queue.enqueue("fahim")
queue.enqueue('afifa')

print(queue.tailElement())

print(queue.data)
