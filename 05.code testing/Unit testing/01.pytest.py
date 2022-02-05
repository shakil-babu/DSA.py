def average(arr):
    if not arr:
        return None

    return sum(arr) / len(arr)


def test_average():
    li = [1, 2, 3, 4]
    expectedResult = 2.5  # wrong case by me
    res = average(li)
    assert expectedResult == res, "Average() produced incorrect result"
