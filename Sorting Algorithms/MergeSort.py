# divide and conquer
def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        array = left + right
        l, r, i = 0, 0, 0
        while l != len(left) and r != len(right):
            if left[l] < right[r]:
                array[i] = left[l]
                i, l = i + 1, l + 1
            else:
                array[i] = right[r]
                i, r = i + 1, r + 1
        while l != len(left):
            array[i] = left[l]
            i, l = i + 1, l + 1
        while r != len(right):
            array[i] = right[r]
            i, r = i + 1, r + 1
    return array
