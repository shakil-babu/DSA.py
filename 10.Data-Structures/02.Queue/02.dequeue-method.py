# dequeue method
def dequeue(self):
    if len(self.data):
        return self.data.pop(0)
    else:
        return "dequeue failed!"
