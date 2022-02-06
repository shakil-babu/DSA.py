def linearSearch(arr, target):
    if not arr:
        return None

    for i in range(len(arr)):
        if target == arr[i]:
            return i

    return -1
