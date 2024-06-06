class Heap:
    def __init__(self):
        self.array = []
        self.size = 0

    def __str__(self):
        return str(self.array)

    @staticmethod
    def is_heap(array):
        for i in range(len(array)):
            left, right = i * 2 + 1, i * 2 + 2
            if (
                left < len(array) and array[i] < array[left] or
                right < len(array) and array[i] < array[right]
            ):
                return False
        return True

    @staticmethod
    def heapify(array):
        length = len(array)
        start = (length // 2) - 1

        def _heapify(i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < length and array[left] > array[largest]:
                largest = left
            if right < length and array[right] > array[largest]:
                largest = right
            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                _heapify(largest)

        for i in range(start, -1, -1):
            _heapify(i)
        return array

    @staticmethod
    def sort(array, order="descending"):
        heap = Heap()
        for i in array:
            heap.insert(i)
        sorted_array = [heap.remove() for i in range(len(array))]
        if order == "ascending":
            sorted_array.reverse()
        return sorted_array

    @staticmethod
    def get_kth_largest(array, kth):
        heap = Heap()
        for i in array:
            heap.insert(i)
        for i in range(kth - 1):
            heap.remove()
        return heap.remove()

    def parent(self, index=None):
        if not index:
            return (self.size - 2) // 2
        return (index - 1) // 2

    def children(self, parent):
        return parent * 2 + 1, parent * 2 + 2

    def swap(self, child, parent):
        self.array[parent], self.array[child] = self.array[child], self.array[parent]

    def bubble_up(self, child, parent):
        if self.array[child] > self.array[parent] and child > 0:
            self.swap(child, parent)
            self.bubble_up(parent, self.parent(parent))

    def bubble_down(self, parent):
        left, right = self.children(parent)
        if left < self.size and self.array[parent] < self.array[left]:
            self.swap(parent, left)
            self.bubble_down(left)
        if right < self.size and self.array[parent] < self.array[right]:
            self.swap(parent, right)
            self.bubble_down(right)

    def insert(self, value):
        self.array.append(value)
        self.size += 1
        self.bubble_up(self.size - 1, self.parent())

    def remove(self):
        root = self.array[0]
        self.swap(0, self.size - 1)
        self.array.pop()
        self.size -= 1
        self.bubble_down(0)
        return root
