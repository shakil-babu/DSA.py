def binarySearch(arr, target):
    if not arr:
        return None

    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # integer division
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1

        if arr[mid] > target:
            right = right - 1

    return -1


def testCases():
    testcases = [
        {
            "name": "simple case 1",
            "arr": [1, 2, 3, 4, 5],
            "target": 4,
            "ans": 3
        },
        {
            "name": "simple case 2",
            "arr": [1, 2, 3, 4],
            "target": 5,
            "ans": -1
        },
        {
            "name": "simple case 3",
            "arr": [],
            "target": 4,
            "ans": None
        }

    ]

    for item in testcases:
        assert item['ans'] == binarySearch(
            item['arr'], item['target']), "Problem on " + item['name']
