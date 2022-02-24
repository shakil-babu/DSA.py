class MaxHeap:
    def __init__(self):
        self.values = []

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

    # _maxHeapify method
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

    # exactMax method
    def _exactMax(self):
        maxElement = self.values[0]
        self.values[0] = self.values.pop()
        self._maxHeapify()
        return maxElement

    # size method
    def _size(self):
        return len(self.values)

    # isEmpty method
    def _isEmpty(self):
        return len(self.values) == 0

    # getMax method
    def _getMax(self):
        if len(self.values) == 0:
            return "Heap is empty!"
        else:
            return self.values[0]

    # print heap
    def _printHeap(self):
        print(self.values)


# initialization
maxheap = MaxHeap()

# insertion
maxheap._insert(100)
maxheap._insert(200)
maxheap._insert(1000)


print(maxheap._exactMax())
# print
maxheap._printHeap()
