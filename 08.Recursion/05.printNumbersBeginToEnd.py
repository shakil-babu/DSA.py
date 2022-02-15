def printBeginToEnd(n):
    if n == 0:
        return
    print(n)
    return printBeginToEnd(n-1)


# initialization
ans = printBeginToEnd(5)
print(ans)
