class HashTable :
    def __init__(self) :
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]
    
    # hashfunction
    def __hashing__(self, key) :
        h = 0
        for char in key :
            h += ord(char)

        return h % self.Max


    # setItem method
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
            
    # get item
    def __getItem__(self, key) :
        hash = self.__hashing__(key)

        for item in self.arr[hash]:
            if item[0] == key :
                return item[1]

    # delete item
    def __deleteItem__(self, key) :
        hash = self.__hashing__(key)
        for idx,element in enumerate(self.arr[hash]):
            if element[0] == key :
                del self.arr[hash][idx]             

    # print
    def Output(self) :
        print(self.arr)

# instance
hashtable = HashTable()


# insert data
hashtable.__setItem__("abc", 1001)
hashtable.__setItem__("bac", 1111)

hashtable.__setItem__("baby", 10020)
hashtable.__setItem__("bayb", 100)
hashtable.__setItem__("fahim", 39002)


# get item
a = hashtable.__getItem__('fahim')
# print(a)
# hashtable.Output()

hashtable.__deleteItem__('baby');
hashtable.Output()
