def binarySearch(arr, target):
    if not arr:
        return None

    left, right = 0, len(arr) - 1
    while left <= right:
        mid1 = left + (right - left) // 3  # integer division
        mid2 = right - (right - left) // 3  # integer division

        if arr[mid1] == target:
            return mid1

        if arr[mid2] == target:
            return mid2

        if arr[mid2] < target:
            left = mid2 + 1
        elif arr[mid1] > target:
            right = mid1 - 1
        else:
            left = mid1 + 1
            right = mid2 - 1

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
