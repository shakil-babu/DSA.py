def selectionSort(arr):
    for i in range(len(arr) - 1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]

    return arr
