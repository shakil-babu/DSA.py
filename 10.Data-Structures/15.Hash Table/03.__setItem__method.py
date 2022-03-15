def __setItem__(self,key, val) :
    hash = self.__hashing__(key)
    self.arr[hash] = val
