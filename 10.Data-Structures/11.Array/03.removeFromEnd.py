def removeFromEnd(self):
    if self.length == 0:
        return "Array is empty!"
    else:
        self.length -= 1
        return self.data.pop()
