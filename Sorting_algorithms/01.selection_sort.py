def selectionSort(arr):
    for i in range(len(arr) - 1):
        largest = i
        for j in range(i+1, len(arr)):
            if arr[largest] < arr[j]:
                largest = j

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
    return arr


sorted = selectionSort([100, 400, 300, 500, 600])
print(sorted)
