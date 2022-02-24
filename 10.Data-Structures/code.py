class MinHeap:
    def __init__(self):
        self.values = []

    # insert method
    def _insert(self, val):
        self.values.append(val)
        self._bubbleUp()

    # bubbleUp method
    def _bubbleUp(self):
        idx = len(self.values) - 1
        element = self.values[idx]
        while idx > 0:
            parentIdx = (idx - 1) // 2
            parentElement = self.values[parentIdx]
            if parentElement < element:
                break
            else:
                self.values[idx] = parentElement
                self.values[parentIdx] = element
                idx = parentIdx

    # minHepify method
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

    # exactmin method
    def _exactMin(self):
        minNumber = self.values[0]
        self.values[0] = self.values.pop()
        self._minHeapify()
        return minNumber

    # size method
    def _size(self):
        return len(self.values)

    # isEmpty method
    def _isEmpty(self):
        return len(self.values) == 0


    # getMin method
    def _getMin(self) :
        if len(self.values) == 0 :
            return "Heap is empty!"

        else :
            return self.values[0]