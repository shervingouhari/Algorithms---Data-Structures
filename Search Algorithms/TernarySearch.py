def ternary_search(array, item):
    def _ternary_search(start, end):
        if start > end:
            return -1
        partition = round((end - start) / 3)
        middle1 = start + partition
        middle2 = end - partition
        if item < array[middle1]:
            return _ternary_search(start, middle1 - 1)
        elif item > array[middle1] and item < array[middle2]:
            return _ternary_search(middle1 + 1, middle2 - 1)
        elif item > array[middle2]:
            return _ternary_search(middle2 + 1, end)
        else:
            if array[middle1] == item:
                return middle1
            elif array[middle2] == item:
                return middle2
    return _ternary_search(0, len(array) - 1)
