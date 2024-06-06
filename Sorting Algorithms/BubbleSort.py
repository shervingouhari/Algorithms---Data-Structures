def bubble_sort(array):
    for iteration in range(1, len(array)):
        is_sorted = True
        for i in range(len(array) - iteration):
            if array[i + 1] < array[i]:
                array[i + 1], array[i] = array[i], array[i + 1]
                is_sorted = False
        if is_sorted:
            break
    return array
