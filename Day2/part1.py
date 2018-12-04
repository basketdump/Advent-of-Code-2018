# Using an array instead of list since fix sized and all integers
from array import array


# Method to zero out our array elements.
def zero_out(arr):
    for i in range(len(arr)):
        arr[i] = 0

    return


# Our integer array that represents a count of alphabet letters
letterCount = array('i', range(26))

# Our counts of strings with exactly two of the same letters and/or three of the same letters
twoCount = 0
threeCount = 0

# Open our input file
with open('input.txt') as inputFile:
    # Read each line of input
    for line in inputFile:
        # Zero out our array so counts are reset for each new line of input
        zero_out(letterCount)
        for ch in line:
            # Ensure this is a lowercase, alphabetic, character
            if 'a' <= ch <= 'z':
                # Add to corresponding letterCount index
                letterCount[ord(ch) - ord('a')] += 1

        # Set these flags since we can only count a pair, or trio, of same letters once.
        # No reason to iterate through rest of array if we have found a pair and trio before the end.
        foundTwo = False
        foundThree = False

        # Loop through our letter counts and increment our twoCount & threeCount accordingly. Will exit if
        # have found a pair and trio already.
        for e in letterCount:
            if e == 2 and not foundTwo:
                twoCount += 1
                foundTwo = True
            elif e == 3 and not foundThree:
                threeCount += 1
                foundThree = True
            elif foundTwo and foundThree:
                break

# Print our checksum
print("twos:", twoCount)
print("threes:", threeCount)
print("Checksum:", twoCount * threeCount)
