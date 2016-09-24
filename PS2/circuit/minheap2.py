class MinHeap:
    """Array-based min-heap implementation """
    def __init__(self):
        # Initially empty heap
        # empty heap is trivially sorted
        self.heap = [0]
        self.size = 0

    def __len__(self):
        # number of elements in heap
        return self.size

    def _min_heapify(self, i):
        # Creates a min heap starting at index i, assuming children are 
        # already min heaps
        left = 2*i
        right = 2*i+1

        if left <= self.size and self.heap[left] < self.heap[i]:
                smallest = left
        else:
            smallest = i
        if right <= self.size and self.heap[right] < self.heap[smallest]:
                smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._min_heapify(smallest)

    def _build_min_heap(self):
        # uses min_heapify starting from the bottom to sort the full heap
        for i in xrange(self.size/2, 0, -1):
            self._min_heapify(i)

    def append(self,val):
        # adds a value to the heap. This causes the heap to become unsorted
        if val is None:
            raise ValueError('Cannot insert None in the heap')
        self.heap.append(val)
        self.size += 1
        self._bubble_up(self.size)

    def _bubble_up(self,child):
        parent = child/2
        if parent > 0:
            if self.heap[child] < self.heap[parent]:
                self.heap[child],self.heap[parent] = self.heap[parent],self.heap[child]
                self._bubble_up(parent)

    def min(self):
        # returns the minimum element of the min heap
        return self.heap[1]

    def pop(self):
        # pops the minimum element of the min heap
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        result = self.heap.pop()
        self.size -= 1
        self._min_heapify(1)
        return result

test = MinHeap()
test.append(10)
test.append(4)
test.append(6)
test.append(5)
test.append(3)
test.append(1)