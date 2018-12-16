import sys
from polymer import Polymer


def main(input_file):
    with open(input_file) as f:
        input_string = f.readline().strip()
    
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
    for c in range(ord('a'), ord('z')+1):
        tmp = Polymer(input_string)
        tmp.remove_type(chr(c))
        tmp.react()

        if shortest_poly is None or tmp.length() < shortest_poly:
            shortest_poly = tmp.length()
    
    print('Shortest possible altered polymer:', shortest_poly)


main(sys.argv[1])
