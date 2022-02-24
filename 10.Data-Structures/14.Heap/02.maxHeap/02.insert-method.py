# insert method
def _insert(self, val):
    self.values.append(val)
    self._bubbleUp()

# bubble up


def _bubbleUp(self):
    idx = len(self.values) - 1
    element = self.values[idx]
    while idx > 0:
        parentIndex = (idx - 1) // 2
        parentElement = self.values[parentIndex]

        if parentElement > element:
            break
        else:
            self.values[idx] = parentElement
            self.values[parentIndex] = element
            idx = parentIndex
