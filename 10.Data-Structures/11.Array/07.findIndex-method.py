def findIndex(self, val):
    for i in range(len(self.data)):
        if self.data[i] == val:
            return i

    return -1
