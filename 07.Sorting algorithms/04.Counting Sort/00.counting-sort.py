from collections import Counter


def countingSort(arr):
    c = Counter(arr)
    minv = min(c.keys())
    maxv = max(c.keys())

    sortedList = []
    for i in range(minv, maxv):
        sortedList.extend([i] * c[i])
    return sortedList


# initialization
sorting = countingSort([3, 4, 6, 2, -1, -1, -2, -3, 4, 4, ])
print(sorting)
