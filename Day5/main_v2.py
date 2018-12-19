import sys
from time import time
from polymer_v3 import Polymer


def main(input_file):
    with open(input_file) as f:
        input_string = f.readline().strip()
    
    start = time()
    # 
    # Part 1
    #
    poly = Polymer(input_string)
    print('Length before reaction:', poly.length())
    poly.react()
    print('Length after reaction:', poly.length())
    # print(str(poly))

    #
    # Part 2
    #
    shortest_poly = None

    # Go through each type, aka, letter and remove it from our temporary polymer
    for c in range(ord('a'), ord('z')+1):
        tmp = Polymer(input_string)
        tmp.remove_type(chr(c))
        tmp.react()

        # If temporary polymer is shorter than shortest length found yet, updated our shortest_poly
        if shortest_poly is None or tmp.length() < shortest_poly:
            shortest_poly = tmp.length()
    
    print('Shortest possible altered polymer:', shortest_poly)
    end = time()
    print("Seconds:", (end - start))

main(sys.argv[1])
