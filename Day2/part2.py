# Using an array instead of list since fix sized and all integers
from array import array


def checkIDs(id1, id2):
    mismatch = -1
    for i in range(len(id1)):
        if id1[i] != id2[i]:
            if mismatch != -1:
                return -1
            else:
                mismatch = i
    
    return mismatch


def getCommonLetters(id, pos):
    return id[0:pos] + id[pos+1:len(id)]


def main():
    answer = None
    ids = []
    
    with open('input.txt') as f:
        ids = f.read().split()

    while len(ids) > 3 and answer == None:
        id1 = ids[0]
        for id2 in ids[1:]:
            chk = checkIDs(id1, id2)
            if (chk != -1):
                answer = getCommonLetters(id1, chk)
                break
        ids.pop(0)
    if answer == None:
        answer = getCommonLetters(ids[0], checkIDs(ids[0], ids[1]))
    
    print(answer)
    print("Length:", len(answer))

main()
