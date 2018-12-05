# Compare our two IDs
def checkIDs(id1, id2):
    # Set mismatch to -1 since that is an impossible location in a string
    # We will return -1 if no mismatches.
    # We will return -1 if mismatch is written to more than once
    mismatch = -1
    for i in range(len(id1)):
        if id1[i] != id2[i]:
            if mismatch != -1:
                return -1
            else:
                mismatch = i
    
    return mismatch


# Print the result of concatenating the substring below pos and the substring above pos
def getCommonLetters(id, pos):
    return id[0:pos] + id[pos+1:len(id)]


def main():
    # init local vars
    answer = None
    ids = []
    
    # Setup ids to hold each line of file
    with open('input.txt') as f:
        ids = f.read().split()

    # Quit if IDs <= 2, because remaining 2 MUST be pair
    # If answer found, don't continue
    while len(ids) > 2 and answer == None:
        id1 = ids[0]
        # Compare id1 via checkIDs with rest of IDs in list
        for id2 in ids[1:]:
            chk = checkIDs(id1, id2)
            # if chk is not -1, we met criteria. Set answer
            if (chk != -1):
                answer = getCommonLetters(id1, chk)
                break
        # Remove current ids[0], aka id1, as it has no pairs.
        ids.pop(0)
    
    # If answer None, remaining IDs are pair
    if answer == None:
        answer = getCommonLetters(ids[0], checkIDs(ids[0], ids[1]))
    
    print(answer)
    print("Length:", len(answer))

main()
