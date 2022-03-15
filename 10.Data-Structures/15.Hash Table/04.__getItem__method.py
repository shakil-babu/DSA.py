def __getItem__(self, key) :
    hash = self.__hashing__(key)
    return self.arr[hash]
