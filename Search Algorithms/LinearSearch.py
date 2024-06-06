def linear_search(array, item):
    for i in range(len(array)):
        if item == array[i]:
            return i
    return -1
