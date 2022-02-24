def _exactMin(self):
    minNumber = self.values[0]
    self.values[0] = self.values.pop()
    self._minHeapify()
    return minNumber
