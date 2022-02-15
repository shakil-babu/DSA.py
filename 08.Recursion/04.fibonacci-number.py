def fibo(n):
    if n in [1, 2]:
        return 1
    return fibo(n - 2) + fibo(n-1)


# initialization
ans = fibo(5)
print(ans)
