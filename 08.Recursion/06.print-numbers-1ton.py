# recursion practice
def printNumbersOneToEnd(n):
    if n == 0:
        return
    printNumbersOneToEnd(n-1)
    print(n)


# initialization
ans = printNumbersOneToEnd(5)
print(ans)
