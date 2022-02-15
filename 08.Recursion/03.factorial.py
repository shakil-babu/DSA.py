# recursion practice
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# initialization
ans = fact(5)
print(ans)
