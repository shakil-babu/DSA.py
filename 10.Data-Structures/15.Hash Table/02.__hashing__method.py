def __hashing__(self, key) :
    h = 0
    for char in key :
        h += ord(char)

    return h % self.Max
