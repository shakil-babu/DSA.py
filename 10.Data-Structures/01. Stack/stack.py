class Stack:
    def __init__(self):
        self.data = []

    # push method

    def push(self, item):
        self.data.append(item)

    # pop method

    def pop(self):
        if(len(self.data)):
            return self.data.pop()
        else:
            return "Pop failed!"

    # is_empty method

    def isEmpty(self):
        return len(self.data) == 0

    # size method
    def size(self):
        return len(self.data)

    # topElement

    def topElement(self):
        if(len(self.data)):
            return self.data[0]
        else:
            return "stack is empty!"

    # tailElement
    def tailElement(self):
        if(len(self.data)):
            return self.data[-1]

        else:
            return "stack is empty!"


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.tailElement())

print(stack.data)
