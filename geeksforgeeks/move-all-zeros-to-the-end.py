def pushZerosToEnd(self, arr, n):
    c = arr.count(0)
    l = []
    for i in arr:
        if i != 0:
            l.append(i)
    for i in range(c):
        l.append(0)

    for i in range(n):
        arr[i] = l[i]

    return arr
