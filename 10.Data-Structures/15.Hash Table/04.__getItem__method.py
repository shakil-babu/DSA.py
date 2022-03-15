# def __getItem__(self, key) :
#     hash = self.__hashing__(key)
#     return self.arr[hash]


def __getItem__(self, key) :
        hash = self.__hashing__(key)

        for item in self.arr[hash]:
            if item[0] == key :
                return item[1]
