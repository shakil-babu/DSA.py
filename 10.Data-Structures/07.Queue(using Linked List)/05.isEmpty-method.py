"""
def isEmpty(self):
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next

        return counter == 0
"""


def isEmpty(self):
    return self.length == 0
