# # # 10 neat python tricks


# 01. reverse string in python
import itertools

a = 'shakil'
rev = a[::-1]















# # # 07. multiply
# # print("str" * 4)





# # # 09 -> take multiple input
# # result = map(lambda x: int(x), raw_input().split())

# # from collections import Counter


# # def findOriginalArray(changed):
# #     if changed is None or len(changed) == 1:
# #         return []
# #     counter = Counter(changed)
# #     ans = []

# #     for key in sorted(counter.keys()):
# #         print(key)
# #         while counter[key] > 0:
# #             counter[key] -= 1
# #             counter[key * 2] -= 1

# #             ans.append(key)


# #         if counter[key * 2] < 0 :
# #             return []

# #     return ans


# from collections import Counter


# def prefixCount(s, t):
#     # sCounter = collections.Counter(s)
#     # tCounter = collections.Counter(t)

#     # for k in tCounter.keys():
#     #     if k in sCounter:
#     #         tCounter[k] -= sCounter[k]
#     #         sCounter[k] = 0
#     # count = 0
#     # for k, v in tCounter.items():
#     #     if v > 0:
#     #         count += v
#     # return count

#     scounter = Counter(s)
#     tcounter = Counter(t)
#     ldef = scounter - tcounter
#     rdef = tcounter - scounter

#     lsum = sum(ldef.values())
#     rsum = sum(rdef.values())

#     return ldef+rsum


# # initialize
# ans = prefixCount('leetcode', 'coats')
# print(ans)


# """

# """


t = int(input())
for i in range(t):
    a, b = input().split()

    a = int(a)
    b = int(b)

    if b == 1 and b >= a:
        print(0)

    elif a < b :
        

