# def findMin(self):
#     if self.root is None:
#         return "Not found!"
#     else:
#         cur = self.root
#         prev = cur
#         while cur:
#             prev = cur
#             cur = cur.left
#         return prev.val


def getMin(self):
    if self.root is None:
        return "Not Found!"
    else:
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val
