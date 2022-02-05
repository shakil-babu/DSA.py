def average(arr):
    if not arr:
        return None

    return sum(arr) / len(arr)


if __name__ == "__main__":
    li = [1, 2, 3, 4]
    expectedResult = 2  # wrong case by me
    res = average(li)
    assert expectedResult == res, "Average() produced incorrect result"
