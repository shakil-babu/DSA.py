def _exactMax(self):
    maxElement = self.values[0]
    self.values[0] = self.values.pop()
    self._maxHeapify()
    return maxElement
