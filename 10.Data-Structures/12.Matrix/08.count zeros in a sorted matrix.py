def countZeroes(self, A, N):
    li = 0
    for item in A:
        z = item.count(0)
        li += z

    return li
