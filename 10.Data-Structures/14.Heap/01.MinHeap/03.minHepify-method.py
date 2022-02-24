def _minHeapify(self, index=0):
    left = 2 * index + 1
    right = 2 * index + 2

    smallest = index
    length = len(self.values)

    # if len is gretor than left and left value less than smallest/root value
    if left < length and self.values[smallest] > self.values[left]:
        smallest = left

    # if len is gretor than right and right value less than smallest/root value
    if right < length and self.vlaues[smallest] > self.vlaues[right]:
        smallest = right

    if smallest != index:
        temp = self.values[index]
        self.values[index] = self.values[smallest]
        self.values[smallest] = temp

        # recursively called
        self._minHeapify(smallest)
