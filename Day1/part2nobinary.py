import time


def search(array, element):
    for e in array:
        if element == e:
            return True
    return False


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
        if search(frequencies, currentFrequency):
            # Yes, break out of loop and print the current frequency
            flag = False
            break
        else:
            # No, insert it into our sorted list
            frequencies.append(currentFrequency)

print("Execution time: ", time.time() - tStart, "s", sep='')
print("# of frequencies found:", len(frequencies))
print("First repeated frequency:", currentFrequency)
