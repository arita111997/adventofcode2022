import re

# Open the input file and split it into two parts: the grid and the instructions
p = open("adventofcode\day22\data22.txt").read().split("\n\n")

def p1():
    # Initialize an empty dictionary to store the tiles of the grid
    k = {}
    # Initialize a variable to store the current direction the robot is facing
    togo = 0
    # Initialize a dictionary to store the movements corresponding to each direction
    m = {
        0: (1, 0),  # right
        1: (0, 1),  # down
        2: (-1, 0), # left
        3: (0, -1), # up
    }
    # Add the tiles of the grid to the dictionary
    for y, o in enumerate(p[0].splitlines()):
        for x, i in enumerate(o):
            if i in [".", "#"]:
                if len(k) == 0:   # store the initial position of the robot
                    lm = (x, y)
                k[(x, y)] = i
    # Extract the instructions from the input file
    trail = re.findall(r"\w?\d+", p[1])

    # Iterate over the instructions
    for h in trail:
        if "R" in h:  # turn right
            togo = (togo + 1) % 4
            h = h.replace("R", "")
        elif "L" in h: # turn left
            togo = (togo - 1) % 4
            h = h.replace("L", "")

        # Move forward the specified number of spaces
        for _ in range(int(h)):
            # Check if the next tile is in the dictionary
            if (lm[0] + m[togo][0], lm[1] + m[togo][1]) in k:
                # If the next tile is a wall, break out of the loop
                if k[(lm[0] + m[togo][0], lm[1] + m[togo][1])] == ".":
                    lm = (lm[0] + m[togo][0],
                           lm[1] + m[togo][1])
                else:
                    break
                # If the next tile is an open space, update the position of the robot
            else:
                # If the robot is facing the top or bottom of the grid,
                #find the x-coordinate of the closest tile on the same y-coordinate
                if togo in [0, 2]:
                    # Find the minimum and maximum x-coordinate of tiles on the same y-coordinate as the robot
                    x = {
                        0: min([tile[0] for tile in k if tile[1] == lm[1]]),
                        2: max([tile[0] for tile in k if tile[1] == lm[1]]),
                        }
                    # Set the position of the robot to the closest tile
                    xmas = (x[togo], lm[1])
                     # If the robot is facing the left or right side of the grid,
                     # find the y-coordinate of the closest tile on the same x-coordinate
                else:
                     # Find the minimum and maximum y-coordinate of tiles on the same x-coordinate as the robot
                     y = {1: min([tile[1] for tile in k if tile[0] == lm[0]]),
                        3: max([tile[1] for tile in k if tile[0] == lm[0]]),}

                     # Set the position of the robot to the closest tile
                     xmas = (lm[0], y[togo])

                # If the tile is an open space, update the position of the robot
                if k[xmas] == ".":
                    lm = xmas
                    # If the tile is a wall, break out of the loop
                else:
                    break

        # Check that the position of the robot is in the dictionary and that the value of the tile is an open space
        assert(lm in k and k[lm] == ".")

    # Print the final position of the robot as a single integer value
    print(1000*(lm[1]+1) + 4 * (lm[0]+1) + togo)


def face(p):
    # Unpack the x and y coordinates of the tile
    x, y = p
    
    # If the y-coordinate is in the top row of the grid,
    # return the number of the grid the tile belongs to
    if y // 50 == 0:
        return x // 50
    # If the y-coordinate is in the second row of the grid,
    # return 3 (the number of the fourth grid)
    elif y // 50 == 1:
        return 3
    # If the y-coordinate is in the third row of the grid,
    # return the number of the grid the tile belongs to
    elif y // 50 == 2:
        return {0: 5, 1: 4}[x // 50]
    # If the y-coordinate is in the bottom row of the grid,
    # return 6 (the number of the sixth grid)
    else:
        return 6


def p2():
    # Initialize an empty dictionary to store the tiles and the direction the robot is facing
    k = {}
    togo = 0
    # Define the movement directions as tuples
    m = {
        0: (1, 0),   # right
        1: (0, 1),   # down
        2: (-1, 0),  # left
        3: (0, -1),  # up
    }
   
    # Define a dictionary to store the wrapping rules for each grid
    wrap = {
        (1, 2): (0, lambda x, y: (0, 149 - y)),   # from grid 1, facing down, to grid 0
        (1, 3): (0, lambda x, y: (0, x+100)),     # from grid 1, facing left, to grid 0
        (2, 0): (2, lambda x, y: (99, 149-y)),    # from grid 2, facing right, to grid 2
        (2, 1): (2, lambda x, y: (99, x-50)),     # from grid 2, facing down, to grid 2
        (2, 3): (3, lambda x, y: (x-100, 199)),   # from grid 2, facing left, to grid 3
        (3, 0): (3, lambda x, y: (y+50, 49)),     # from grid 3, facing right, to grid 3
        (3, 2): (1, lambda x, y: (y-50, 100)),    # from grid 3, facing down, to grid 1
        (4, 0): (2, lambda x, y: (149, 149-y)),   # from grid 4, facing right, to grid 2
        (4, 1): (2, lambda x, y: (49, 100+x)),    # from grid 4, facing down, to grid 2
        (5, 2): (0, lambda x, y: (50, 149-y)),    # from grid 5, facing down, to grid 0
        (5, 3): (0, lambda x, y: (50, 50+x)),     # from grid 5, facing left, to grid 0
        (6, 0): (3, lambda x, y: (y-100, 149)),   # from grid 6, facing right, to grid 3
        (6, 1): (1, lambda x, y: (x+100, 0)),     # from grid 6, facing down, to grid 1
        (6, 2): (1, lambda x, y: (y-100, 0)),     # from grid 6, facing left, to grid 1
    }
    # Iterate through the rows and columns of the grid
    for y, o in enumerate(p[0].splitlines()):
        for x, i in enumerate(o):
            if i in [".", "#"]:
                # If the current tile is a valid tile, store it in the dictionary
                if len(k) == 0:
                    # If the dictionary is empty, store the current tile as the starting location
                    lm = (x, y)
                k[(x, y)] = i

    # Find all the instructions in the input string
    trail = re.findall(r"\w?\d+", p[1])

    # If the instruction is a right turn, update the direction the robot is facing
    for h in trail:
        if "R" in h:
            togo = (togo + 1) % 4
            h = h.replace("R", "")
            # If the instruction is a left turn, update the direction the robot is facing
        elif "L" in h:
            togo = (togo - 1) % 4
            h = h.replace("L", "")
            # For the number of steps specified in the instruction, move the robot in the current direction

        for _ in range(int(h)):
            # If the next tile in the current direction is a valid tile, move the robot to that tile
            if (lm[0] + m[togo][0], lm[1] + m[togo][1]) in k:
                # If the next tile in the current direction is a valid tile, move the robot to that tile
                if k[(lm[0] + m[togo][0], lm[1] + m[togo][1])] == ".":
                    lm = (lm[0] + m[togo][0], lm[1] + m[togo][1])
                    # If the next tile is not a valid tile, stop moving
                else:
                    break
            else:
                # If the next tile is not a valid tile, find the corresponding tile in the adjacent panels
                xnas, co = wrap[(face(lm), togo)]
                xmas = co(lm[0], lm[1])
                # Assert that the corresponding tile is a valid tile
                assert(xmas in k)
                # If the corresponding tile is not a valid tile, do nothing
                if xmas not in k:
                    pass
                # If the corresponding tile is a valid tile, 
                # move the robot to that tile and update the direction the robot is facing
                if k[xmas] == ".":
                    togo = xnas
                    lm = xmas
                    # If the corresponding tile is not a valid tile, stop moving
                else:
                    break
    # Calculate the final position of the robot and print it
    print(1000*(lm[1]+1) + 4 * (lm[0]+1) + togo)


if __name__ == "__main__":
    # Call the p1 function
    p1()
    # Call the p2 function
    p2()
    

    