def GCD(a, b):
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    print('GCD is:', b)
    return b


print(GCD(480, 30))


# shortest
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(gcd(480, 30))
