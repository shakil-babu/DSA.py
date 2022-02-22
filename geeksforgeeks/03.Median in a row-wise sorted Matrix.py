
def median(self, matrix, r, c):
    li = []
    for item in matrix:
        li += item

    li.sort()

    mid = len(li) // 2

    return li[mid]
