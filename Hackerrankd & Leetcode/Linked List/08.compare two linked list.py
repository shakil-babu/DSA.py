def compare_lists(llist1, llist2):
    a, b = llist1, llist2
    while a and b:
        if a.data == b.data:
            a = a.next
            b = b.next
        else:
            return 0

    if a == None and b == None:
        return 1
    else:
        return 0
