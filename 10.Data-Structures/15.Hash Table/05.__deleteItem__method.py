def __deleteItem__(self, key) :
    hash = self.__getItem__(key)
    self.arr[hash] = None
