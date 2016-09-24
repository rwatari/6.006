#import pdb

class MinHeap:
    """Array-based min-heap implementation """
    def __init__(self):
        # Initially empty heap
        # empty heap is trivially sorted
        self.heap = []
        self.sorted = True

    def __len__(self):
        # number of elements in heap
        return len(self.heap)

    def _min_heapify(self, i):
        # Creates a min heap starting at index i, assuming children are 
        # already min heaps
        left = 2*(i+1)-1
        right = 2*(i+1)

        if left < len(self.heap) and self.heap[left] < self.heap[i]:
                smallest = left
        else:
            smallest = i
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest)

    def _build_min_heap(self):
        # uses min_heapify starting from the bottom to sort the full heap
        for i in xrange(len(self.heap)/2, -1, -1):
            self._min_heapify(i)
        self.sorted = True

    def append(self,val):
        # adds a value to the heap. This causes the heap to become unsorted
        if val is None:
            raise ValueError('Cannot insert None in the heap')
        self.heap.append(val)
        self.sorted = False

    def min(self):
        # returns the minimum element of the min heap
        if self.sorted:
            return self.heap[0]
        else:
            self._build_min_heap()
            return self.heap[0]

    def pop(self):
        # pops the minimum element of the min heap
        if self.sorted:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            result = self.heap.pop()
            self._min_heapify(0)
            return result
        else:
            self._build_min_heap()
            return self.pop()


test = MinHeap()
test.heap = [6,3,4]
#pdb.set_trace()
test._build_min_heap()
