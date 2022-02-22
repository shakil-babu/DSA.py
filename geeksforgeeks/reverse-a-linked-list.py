def reverseList(self, head):
    # Code here
    if head is None:
        return head

    else:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp

    return prev
