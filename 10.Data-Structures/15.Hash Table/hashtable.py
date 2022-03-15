class HashTable :
    def __init__(self) :
        self.Max = 100
        self.arr = [None for i in range(self.Max)]


    
    # hashfunction
    def __hashing__(self, key) :
        h = 0
        for char in key :
            h += ord(char)

        return h % self.Max


    # setItem method
    def __setItem__(self,key, val) :
        hash = self.__hashing__(key)
        self.arr[hash] = val


    # get item
    def __getItem__(self, key) :
        hash = self.__hashing__(key)
        return self.arr[hash]


    # delete item
    def __deleteItem__(self, key) :
        hash = self.__getItem__(key)
        self.arr[hash] = None



# instance
hashtable = HashTable()


# insert data
hashtable.__setItem__("shakil", 1001)
hashtable.__setItem__("torikus", 10020)
hashtable.__setItem__("fahim", 39002)


# get item
a = hashtable.__getItem__('shakil')
print(a)
