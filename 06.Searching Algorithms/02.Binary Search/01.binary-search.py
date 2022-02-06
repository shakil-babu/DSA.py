def binarySearch(arr, target):
    if not arr:
        return None

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # integer division
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1

        if arr[mid] > target:
            right = right - 1

    return -1
