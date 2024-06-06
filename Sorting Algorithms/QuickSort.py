# divide and conquer
def quick_sort(array):
    def _quick_sort(array, start, end):
        if start >= end:
            return
        boundary = start - 1
        for i in range(start, end + 1):
            if array[i] <= array[end]:
                boundary += 1
                array[i], array[boundary] = array[boundary], array[i]
        _quick_sort(array, start, boundary - 1)
        _quick_sort(array, boundary + 1, end)
    _quick_sort(array, 0, len(array) - 1)
    return array
