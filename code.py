def _hashing(key) :
    hash = 0
    for item in key :
        hash += ord(item)
    
    return hash % 10


# hash
li = [[],[],[],[],[('abc',500)],[],[],[],[],[]]


def _setItem(key,value):
    h = _hashing(key)
    found = False

    for idx,element in enumerate(li[h]):
        if len(element) == 2 and element[0] == key :
            li[h].append((key,value))
            found = True
            break

    if not found:
        li[h].append((key,value))

_setItem('abc',100)
_setItem('uva',1001)
print(li)
