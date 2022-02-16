class Array:
    def __init__(self):
        self.data = []
        self.length = 0

    # insert
    def insert(self, val):
        self.length += 1
        return self.data.append(val)

    # remove

    def removeFromEnd(self):
        if self.length == 0:
            return "Array is empty!"
        else:
            self.length -= 1
            return self.data.pop()

    # remove

    def removeFromBegin(self):
        if self.length == 0:
            return "Array is empty!"
        else:
            self.length -= 1
            return self.data.pop(0)

    # size method

    def size(self):
        return self.length

    # contains

    def contains(self, val):
        if val in self.data:
            return True
        else:
            return False

    # find

    def findIndex(self, val):
        for i in range(len(self.data)):
            if self.data[i] == val:
                return i

        return -1

    # startswith

    def startsWith(self, val):
        if self.data[0] == val:
            return True
        else:
            return False

    # endswith

    def endsWith(self, val):
        if self.data[-1] == val:
            return True
        else:
            return False

    # print
    def Print(self):
        print(self.data)


# initialization
array = Array()
array.insert(10)
array.insert(20)
array.insert(30)
array.insert(40)


array.Print()
print(array.size())
print(array.contains(440))
array.Print()
