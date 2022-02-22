def isRepresentingBST(self, arr, N):
    for i in range(1, N):
        prev = arr[i - 1]
        cur = arr[i]

        if cur <= prev:
            return 0

    return 1
