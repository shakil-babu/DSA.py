def kthSmallest(mat, n, k):
    li = []
    for item in mat:
        li += item
    li.sort()
    return li[k-1]
