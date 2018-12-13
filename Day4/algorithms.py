def binary_search(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if element == array[mid]:
            return mid
        elif element < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_insert(array, element):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if element == array[mid]:
            array.insert(mid, element)
            return mid
        elif element < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if element > array[mid]:
        mid += 1

    array.insert(mid, element)
    return mid


def index_of_max(elements):
    highest = -1
    index = -1
    for i in range(len(elements)):
        current = elements[i]
        if current > highest:
            highest = current
            index = i

    return index
