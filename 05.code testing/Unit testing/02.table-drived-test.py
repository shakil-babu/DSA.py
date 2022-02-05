def average(arr):
    if not arr:
        return None

    return sum(arr) / len(arr)


def test_average():
    test_cases = [
        {
            "name": "simple case 1",
            "input": [1, 2, 3],
            "expected": 2.0
        },

        {
            "name": "simple case 2",
            "input": [1, 2, 3, 4],
            "expected": 2.5
        },
        {
            "name": "simple case 3",
            "input": [100],
            "expected": 100.0
        },
        {
            "name": "simple case 4",
            "input": [],
            "expected": None
        }

    ]

    for testCase in test_cases:
        assert testCase['expected'] == average(
            testCase['input']), testCase['name']
