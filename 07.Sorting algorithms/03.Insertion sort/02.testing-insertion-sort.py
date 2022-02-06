def insertionSort(arr):
    for i in range(1, len(arr)):
        item = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > item:
            arr[j+1] = arr[j]
            j = j - 1
            arr[j+1] = item
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
        assert item['ans'] == insertionSort(
            item['arr']), "Problem on " + item['name']
