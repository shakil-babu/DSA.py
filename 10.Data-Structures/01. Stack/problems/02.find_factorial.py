def fact(n):
    contains = []
    while n > 0:
        contains.append(n)
        n -= 1

    fact = 1
    while len(contains) > 0:
        fact *= contains.pop()

    return fact
