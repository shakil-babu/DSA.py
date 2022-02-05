def isPalindrome(str):
    contains = []
    for item in str:
        contains.append(item)

    word = ""
    while len(contains) > 0:
        word += contains.pop()

    return word == str
