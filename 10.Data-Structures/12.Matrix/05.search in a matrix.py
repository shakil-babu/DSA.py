def matSearch(self,mat, N, M, X):
    i, j = 0, len(mat[0]) - 1
    while j >= 0 and i < N :
        if mat[i][j] == X :
            return 1
        elif mat[i][j] > X :
            j -= 1
        else :
            i += 1
            
    return 0