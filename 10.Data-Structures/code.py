class MinHeap:
    def __init__(self):
        self.values = []

    def _insert(self, val):
        self.values.append(val)
        self._bubbleUp()

    def _bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = idx + 1 // 2
            parentElement = self.values[parentIdx]
            if parentElement < element:
                break
            else:
                self.values[idx] = parentElement
                self.values[parentIdx] = element
                idx = parentIdx

    def _minHeapify(self):
        pass
