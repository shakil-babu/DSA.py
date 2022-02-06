def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

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
        assert item['ans'] == bubbleSort(
            item['arr']), "Problem on " + item['name']
