import time


# Our implementation of binary search
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


# Our implementation of binary insert
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


# Load our file into an array of strings. We delimit initial loaded string by newline
inputFile = open("input.txt")
inputData = inputFile.read()
lines = inputData.split()

# Set our starting frequency and add it to frequencies which holds the frequencies we've already hit
currentFrequency = 0
frequencies = [currentFrequency]
# Set a flag so we can escape our while loop
flag = True

tStart = time.time()
while flag:
    for line in lines:
        currentFrequency += int(line)
        # Is current frequency already in our list of frequencies?
        if binary_search(frequencies, currentFrequency) != -1:
            # Yes, break out of loop and print the current frequency
            flag = False
            break
        else:
            # No, insert it into our sorted list
            binary_insert(frequencies, currentFrequency)
print("Execution time: ", time.time() - tStart, "s", sep='')
print("# of frequencies found:", len(frequencies))
print("First repeated frequency:", currentFrequency)
