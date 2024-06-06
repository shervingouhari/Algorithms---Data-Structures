import heapq


def heap_sort(array):
    heap = []
    for i in range(len(array)):
        heapq.heappush(heap, array.pop())
    for i in range(len(heap)):
        array.append(heapq.heappop(heap))
    return array
