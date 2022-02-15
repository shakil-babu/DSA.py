def sum(arr):
    if len(arr) == 1:
        return arr[0]
    rest = arr[1:]
    return arr[0] + sum(rest)


ans = sum([10, 10, 10])
print(ans)
