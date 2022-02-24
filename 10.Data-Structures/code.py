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
    def _maxHeapify(self):
        pass

    # size method
    def _size(self):
        pass


    # print heap
    def _printHeap(self) :
        print(self.values)

# initialization
maxheap = MaxHeap()

# insertion
maxheap._insert(100)
maxheap._insert(200)
maxheap._insert(1000)


# print 
maxheap._printHeap()