def linearSearch(arr, target):
    if len(arr) < 1:
        return -1

    if arr.pop(0) == target:
        return True

    return linearSearch(arr, target)

    # initialization
ans = linearSearch([10, 20, 30, 40], 50)
print(ans)


# # recursion practice
# def linearSearch(arr, left, right, target):
#     if left > right:
#         return -1

#     if arr[left] == target:
#         return left

#     if arr[right] == target:
#         return right

#     return linearSearch(arr, left + 1, right - 1, target)

#     # initialization
# ans = linearSearch([10, 20, 30, 40], 0, 3, 20)
# print(ans)
