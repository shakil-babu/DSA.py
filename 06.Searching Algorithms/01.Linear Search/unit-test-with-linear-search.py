def linearSearch(arr, target):
    if not arr:
        return None

    for i in range(len(arr)):
        if target == arr[i]:
            return i

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
            "name": "simple case 1",
            "arr": [1, 2, 3, 4],
            "target": 5,
            "ans": -1
        },
        {
            "name": "simple case 1",
            "arr": [],
            "target": 4,
            "ans": None
        }

    ]

    for item in testcases:
        assert item['ans'] == linearSearch(
            item['arr'], item['target']), "Problem on " + item['name']
