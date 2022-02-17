def reversePrint(llist):
    cur = llist
    stack = []
    while cur:
        stack.append(cur.data)
        cur = cur.next

    while len(stack):
        item = stack.pop()
        print(item)
