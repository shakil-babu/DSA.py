def _maxHeapify(self, index=0):
    left = index * 2 + 1
    right = index * 2 + 2

    length = len(self.values)
    largest = index

    if left < length and self.values[largest] < self.values[left]:
        largest = left

    if right < length and self.values[largest] < self.values[right]:
        largest = right

    if largest != index:
        temp = self.values[index]
        self.values[index] = self.values[largest]
        self.values[largest] = temp

        # recursively called
        self._maxHeapify()
