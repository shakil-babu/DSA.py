# Function to search a given number in row-column sorted matrix.
def search(self, matrix, n, m, x):
    # code here
    for item in matrix:
        if x in item:
            return True

    return False
