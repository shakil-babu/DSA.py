
li = [1, 1, 2, 3, 3]


def frequencyCounter(arr):
    count = dict()
    for item in arr:
        if count.get(item):
            count[item] += 1
        else:
            count[item] = 1

    return count


ans = frequencyCounter(li)
print(ans)

# output : {1: 2, 2: 1, 3: 2}

# build in Counter

# from collections import Counter

# li = [1, 1, 2, 3, 4, 2, 2]
# count = Counter(li)

# print(count)
