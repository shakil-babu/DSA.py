def sortedMatrix(self, N, Mat):
    li = []
    for item in Mat:
        li += item

    li.sort()

    x = 0
    for i in range(N):
        for j in range(N):
            Mat[i][j] = li[x]
            x += 1

    return Mat
