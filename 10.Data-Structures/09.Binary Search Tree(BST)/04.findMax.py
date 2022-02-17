# def findMax(self):
#     if self.root is None:
#         return "Not found!"
#     else:
#         cur = self.root
#         prev = cur
#         while cur:
#             prev = cur
#             cur = cur.right
#         return prev.val


def getMax(self):
    if self.root is None:
        return "Not Found!"
    else:
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val
