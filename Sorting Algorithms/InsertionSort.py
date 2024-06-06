def insertion_sort(array):
    for iteration in range(1, len(array)):
        for i in range(iteration, 0, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            else:
                break
    return array
