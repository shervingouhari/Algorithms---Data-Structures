def selection_sort(array):
    for iteration in range(len(array)):
        minimum = iteration
        for i in range(minimum, len(array)):
            if array[i] < array[minimum]:
                minimum = i
        array[iteration], array[minimum] = array[minimum], array[iteration]
    return array
