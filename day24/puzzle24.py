from collections import defaultdict
import heapq


def data():
    # create a dictionary to map character directions to (x, y) tuples
    dct = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
     # read the maze data from a file
    with open(r"adventofcode\day24\data24.txt") as f:
        # get the width and height of the maze
        lines = f.read().splitlines()
        height = len(lines) - 2
        width= len(lines[1]) - 2
        # get the start and end positions of the maze
        start = (lines[0].index(".") - 1, -1)
        end = (lines[-1].index(".") - 1, height)
        # get a list of "cold" tiles and their directions
        cold = [((x-1, y-1), dct[lines[y][x]]) \
            for y in range(1, height+1) for x in range(1, width+1) if lines[y][x] in dct]
            # return the start and end positions, the list of "cold" tiles, and the width and height of the maze
        return start, end, cold, width, height

# check the cache for the positions of the "cold" tiles at this time
def td(cold, time):
    if time in cold_dict: return cold_dict[time]
    # create a defaultdict to store the positions of the "cold" tiles at this time
    ect = defaultdict(list)
    # calculate the positions of the "cold" tiles at this time
    for cold in cold:
        x, y = (cold[0][0] + cold[1][0] * time) % width, \
            (cold[0][1] + cold[1][1] * time) % height
        ect[(x, y)].append(cold)
        # store the positions of the "cold" tiles in the cache
    cold_dict[time] = ect
     # return the positions of the "cold" tiles
    return ect

def calc(ti, cold, time):
    # define the directions that can be moved in
    df = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    # get the positions of the "cold" tiles at the next time step
    ect = td(cold, time+1)
    moves = []
    # iterate over the possible moves
    for da in df:
        x, y = ti[0] + da[0], ti[1] + da[1]
        # if the move is not onto a "cold" tile, and is either the end position,
        #start position, or a valid position on the maze, add it to the list of valid moves
        if (x, y) not in ect and ((x, y) == end or (x, y) == start or  x >= 0 and x < width and y >= 0 and y < height):
            moves.append((x, y))
             # return the list of valid moves
    
    return moves

def fpt(cold, start_ti, end_ti, time):
    # create a heap to store the search state
    heap = []
    # push the start position onto the heap
    heapq.heappush(heap, (0, start_ti, time))
    visited = set() # create a set to store visited positions
     
    # continue searching while the heap is not empty
    while heap:
        # pop the next position from the heap
        _, ti, time = heapq.heappop(heap)
        # check if the position is the end position
        if ti == end_ti:
             # if it is, return the time it took to reach this position
             return time
             # if the position has not been visited before
        if (ti, time) not in visited:
            # mark it as visited
            visited.add((ti, time))
            # get the valid moves from this position
            for move in calc(ti, cold, time):
                # push the valid moves onto the heap, 
                # with the cost function being the distance 
                # to the end position plus the time it took to reach this position
                heapq.heappush(heap, (abs(ti[0] - end_ti[0]) + abs(ti[1] - end_ti[1]) + time, move, time+1))


# get the start and end positions, the "cold" tiles, and the width and height of the maze
start, end, cold, width, height = data()
# create a cache to store the positions of the "cold" tiles at each time
cold_dict = {}

# find the shortest path from the start to the end position,
#  and store the result in the p1 variable
p1 = fpt(cold, start, end, 0)

# print the result
print ("P1:", p1)
# find the shortest path from the end to the start position, and print the result
print ("P2:", fpt(cold, start, end, 
        fpt(cold, end, start, p1)))