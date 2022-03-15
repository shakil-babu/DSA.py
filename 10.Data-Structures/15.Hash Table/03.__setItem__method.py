# def __setItem__(self,key, val) :
#     hash = self.__hashing__(key)
#     self.arr[hash] = val


def __setItem__(self,key, val) :
        hash = self.__hashing__(key)
        found = False
        for idx,element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key :
                self.arr[hash].append((key,val))
                found = True
                break

        if not found:
            self.arr[hash].append((key,val))
