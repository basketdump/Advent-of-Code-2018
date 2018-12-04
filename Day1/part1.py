# Set our starting frequency
currentFrequency = 0

# Load our file using 'with' for best practices. File is closed upon exiting with.
with open("input.txt") as inputFile:
    # Loop through each line, adding the current lines value to currentFrequency,
    # and storing it back into currentFrequency
    for line in inputFile:
        currentFrequency += int(line)

print(currentFrequency)
