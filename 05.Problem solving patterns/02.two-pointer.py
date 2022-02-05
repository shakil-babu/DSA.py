
def twoPointer(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]

        if sum > target:
            right -= 1
        if sum < target:
            left += 1

    return -1


ans = twoPointer([10, 20, 30, 40, 50], 50)
print(ans)

# output : [0, 3]
