def binary_search(array, item):
    def _binary_search(start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if item < array[middle]:
            return _binary_search(start, middle - 1)
        elif item > array[middle]:
            return _binary_search(middle + 1, end)
        return middle
    return _binary_search(0, len(array) - 1)
