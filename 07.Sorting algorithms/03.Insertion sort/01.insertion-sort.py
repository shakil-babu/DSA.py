def insertionSort(arr):
    for i in range(1, len(arr)):
        item = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j - 1
            arr[j+1] = item
    return arr
