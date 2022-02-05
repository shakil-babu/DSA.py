def Avg(arr):
    if not arr:
        return None

    return sum(arr) / len(arr)


if __name__ == "__main__":
    li = [1, 2, 3, 4]
    expected_result = 2.5
    result = Avg(li)

    if expected_result == result:
        print("Accepted")
    else:
        print("Wrong answere!")
