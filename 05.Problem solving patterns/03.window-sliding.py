# window sliding algorithm

def maxSum(arr, n):
    Max, temp = 0, 0
    if len(arr) < n:
        return None

    for i in range(n):
        Max += arr[i]

    temp = Max
    for i in range(n, len(arr)):
        temp = temp - arr[i-n] + arr[i]
        Max = max(Max, temp)

    return Max


ans = maxSum([10, 20, 2, 3, 2, 3], 3)
print(ans)
