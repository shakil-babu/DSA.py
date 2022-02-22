def isPalindrome(self, head):
    values = []
    cur = head
    while cur:
        values.append(cur.data)
        cur = cur.next

    a = ""
    c = values.copy()

    for item in values:
        a += str(item)

    c.reverse()
    b = ""
    for item in c:
        b += str(item)

    return a == b
