from collections import Counter


# def countingSort(arr):
#     c = Counter(arr)
#     minv = min(c.keys())
#     maxv = max(c.keys())

#     sortedList = []
#     for i in range(minv, maxv):
#         sortedList.extend([i] * c[i])
#     return sortedList


# # initialization
# sorting = countingSort([3, 4, 6, 2, -1, -1, -2, -3, 4, 4, ])
# print(sorting)

def merge(a, b):
    i, j = 0, 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(b[j])
            j += 1

    if i < len(a):
        ans.extend(a[i:])
    elif j < len(b):
        ans.extend(b[j:])

    return ans


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = mergeSort(arr[:mid]), mergeSort(arr[mid:])
    return merge(left, right)


# initialization
sorting = mergeSort([5, 2, 3, 1])
print(sorting)
