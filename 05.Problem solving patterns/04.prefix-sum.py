
def prefixSum(li):
    res = [sum(li[: i + 1]) for i in range(len(li))]
    return res


ans = prefixSum([10, 20, 30])
print(ans)
