def rowWithMax1s(self, arr, n, m):
    # code here
    count = arr[0].count(1)

    for item in arr:
        count = max(count, item.count(1))
    if count == 0:
        return -1
    i = 0
    for item in arr:
        if item.count(1) == count:
            break
        i += 1

    return i
