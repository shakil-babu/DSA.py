def selectionSort(arr):
    for i in range(len(arr) - 1):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]

    return arr


def testCases():
    testcases = [
        {
            "name": "simple case 1",
            "arr": [5, 4, 1, 2, 3],
            "ans": [1, 2, 3, 4, 5]
        },
        {
            "name": "simple case 2",
            "arr": [300, 20, 10],
            "ans": [10, 20, 300]
        },
        {
            "name": "simple case 3",
            "arr": [],
            "ans": []
        }

    ]

    for item in testcases:
        assert item['ans'] == selectionSort(
            item['arr']), "Problem on " + item['name']
