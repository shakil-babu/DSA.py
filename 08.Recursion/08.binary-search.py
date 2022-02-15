def binarySearch(arr, left, right, target):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binarySearch(arr, mid + 1, right, target)

    else:
        return binarySearch(arr, left, mid - 1, target)


    # initialization
ans = binarySearch([10, 20, 30, 40], 0, 3, 20)
print(ans)
