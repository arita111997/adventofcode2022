from itertools import cycle
from collections import defaultdict

def data():
    # read the data file and create a set of coordinates representing the positions of the elves
    with open (r'adventofcode\day23\data23.txt') as f:
        return set((x,y) for y, l in enumerate(f.readlines()) for x, c in enumerate(l) if c == '#')

def go(elves, d1):
     # create a defaultdict to keep track of elves trying to move to the same position
    p = defaultdict(list)
    # get the next direction from the d1 iterator
    bg = next(d1)
    # iterate over the elves
    for xmas in elves:
         # check if the elf has any neighboring elves
        if not any((xmas[0] + look[0], xmas[1] + look[1]) in elves for look in hoho):
            continue
        # try to move the elf in each of the four directions (determined by the bg variable)

        for i in range(4):
            damm = False
            # check if there are any neighboring elves in the direction we are trying to move
            for go_to in go_tos[(bg + i) % 4]:
                if (xmas[0] + go_to[0], xmas[1] + go_to[1]) in elves:
                    damm = True
                    break
            # if there are no neighboring elves, move the elf
            if not damm:
                go_to = go_tos[(bg + i) % 4][1] # get the coordinate to move to
                p[(xmas[0] + go_to[0], xmas[1] + go_to[1])].append(xmas) # add the elf to the defaultdict
                break # break out of the loop
    # check the defaultdict for elves trying to move to the same position
    for propose in p:
        # if there is only one elf trying to move to this position, allow it to move
        if len(p[propose]) == 1:
            # remove the elf from its current position
            elves.remove(p[propose][0])
            elves.add(propose) # add the elf to its new position
    
    # return True if there are no more movements possible, False otherwise
    return len(p) == 0

def p1():
    # get the initial positions of the elves
    elves = data()
     # create an iterator that cycles through the numbers 0 through 3
    d1 = cycle(range(4))
     
     # simulate the movement of the elves for 10 rounds
    for _ in range(10):
        go(elves, d1)

    # find the minimum and maximum x and y coordinates of the elves
    min_x = min(elves, key=lambda x: x[0])[0]
    max_x = max(elves, key=lambda x: x[0])[0]
    min_y = min(elves, key=lambda x: x[1])[1]
    max_y = max(elves, key=lambda x: x[1])[1]
    
    # count the number of squares on the grid that do not contain an elf
    return sum((x, y) not in elves for y in range(min_y, max_y + 1) for x in range(min_x, max_x + 1))

def p2():
    # get the initial positions of the elves
    elves = data()
    # create an iterator that cycles through the numbers 0 through 3
    d1 = cycle(range(4))

    round = 0   # variable to keep track of the number of rounds
                
    # simulate the movement of the elves until there are no more movements possible
    while True:
        round += 1         # increment the round counter
        if go(elves, d1):  # check if there are any more movements possible
            break          # if not, break out of the loop
    
    # return the number of rounds that were simulated
    return round

# define lists of coordinates for the four directions that the elves can move in
go_tos = [[(-1, -1), (0, -1), (1, -1)], [(1, 1), (0, 1), (-1, 1)], 
          [(-1, 1), (-1, 0), (-1, -1)], [(1, -1), (1, 0), (1, 1)]
         ]
# define a list of coordinates for the eight positions around an elf
hoho = [(-1,-1), (0,-1), (1,-1), (1,1), (0,1), (-1,1), (-1,0), (1,0)]


# print the results of p1() and p2()
print ("P1:", p1())
print ("P2:", p2())