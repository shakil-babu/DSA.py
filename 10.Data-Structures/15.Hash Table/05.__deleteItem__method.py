# def __deleteItem__(self, key) :
#     hash = self.__getItem__(key)
#     self.arr[hash] = None


def __deleteItem__(self, key) :
        hash = self.__hashing__(key)
        for idx,element in enumerate(self.arr[hash]):
            if element[0] == key :
                del self.arr[hash][idx] 
