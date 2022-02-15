def sum(n):
    if n == 1:
        return 1
    return n + sum(n - 1)


# initialization
ans = sum(4)
print(ans)
