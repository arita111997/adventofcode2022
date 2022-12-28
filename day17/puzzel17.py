import sys


class Game:

    def __init__(self, stream) -> None:
        """
        Initializes a new game with the given stream of moves.
        """
        self.stream = stream
        self.num = 0
        self.id = 0
        self.leftwall = 0
        self.rightwall = 8
        self.h = 0
        self.grid = set()
        for i in range(0,9):
            self.grid.add((i, 0))
        self.new_rock()
        self.sig = {}

    
    def drop1rock(self):
        """
        Drops a single rock and returns the first repeated rock.
        """
        while True:
            self.push(self.stream[self.id] == '<')
            if self.fall():
                break
        siG = self.siG()
        hit = None, None
        if siG in self.sig:
            hit = self.h - self.sig[siG][0], self.num - self.sig[siG][1]
        self.sig[siG] = (self.h, self.num)
        return hit


    def push(self, left=True):
        """
        Pushes the rock left or right.
        """
        dP = -1 if left else 1
        if all(0 < x+dP < 8 for x,y in self.rock) and all((x+dP,y) not in self.grid for x,y in self.rock):
            self.rock = set((x+dP,y) for x,y in self.rock)
        self.id = (self.id + 1) % len(self.stream)


    def fall(self):
        """
        Makes the rock fall down until it reaches the ground or another rock.
        Returns True if the rock landed on the ground or another rock, False otherwise.
        """
        if all((x,y-1) not in self.grid for x,y in self.rock):
            self.rock = set((x,y-1) for x,y in self.rock)
            return False

        self.h = max([y for x,y in self.rock] + [self.h])
        for x,y in self.rock:
            self.grid.add((x,y))
        self.new_rock()
        return True


    def new_rock(self):
        """
        Gets a new rock for the game.
        """
        self.rock = set()
        numr = self.num % 5
        if numr == 0:
            for x in range(3, 7):
                self.rock.add((x, self.h + 4))
        elif numr == 1:
            self.rock.add((3, self.h + 5))
            self.rock.add((4, self.h + 4))
            self.rock.add((4, self.h + 5))
            self.rock.add((4, self.h + 6))
            self.rock.add((5, self.h + 5))
        elif numr == 2:
            for x in range(3,6):
                self.rock.add((x, self.h + 4))
            for y in range(5,7):
                self.rock.add((5, self.h + y))
        elif numr == 3:
            for y in range(4, 8):
                self.rock.add((3, self.h + y))
        elif numr == 4:
            for x in range(3, 5):
                for y in range(4, 6):
                    self.rock.add((x, y + self.h))
        else:
            assert False
        self.num += 1


    def p(self):
        """
        Prints the current state of the game.
        """
        t = max([self.h] + [y for x,y in self.rock]) + 2
        for r in range(t, -1, -1):
            print(f'{r:5} |', end='')
            for c in range(1, 8):
                if (c,r) in self.grid:
                    print('#', end='')
                elif (c,r) in self.rock:
                    print('@', end='')
                else:
                    print(' ', end='')
            print('|')

        
    def siG(self):
        """
        Calculates the signature for the current state of the game.
        """
        rows = 40
        points = set((self.num % 5,))
        for y in range(rows):
            for x in range(1,8):
                if (x, y + self.h - rows) in self.grid:
                    points.add((x,y))
        return frozenset(points)
# Open the file 'adventofcode/day17/data17.txt' in the current working directory
# and assign a file object to the variable 'f'
with open('adventofcode\day17\data17.txt', 'r') as f:
    # Read the contents of the file and store it as a single string in the variable 'line'
    # Strip any leading or trailing white space from the string
    line = f.read().strip()
# Create an instance of the 'Game' class with 'line' as an argument
# and store it in the variable 'game'
game = Game(line)
# Initialize the variable 'drop' with the value of the third command-line argument
# If no third argument is provided, default to 2022
drop = int(sys.argv[2]) if len(sys.argv) > 2 else 2022
# Iterate 'drop' times and call the 'drop1rock()' method on the 'game' object
# on each iteration
for _ in range(drop):
    game.drop1rock()
 # Store the value of 'game.h' in the variable 'part1'
# and print it to the console with the string 'Part 1: ' preceding it   
part1 = game.h
print(f'Part 1: {part1}')
# Create a new instance of the 'Game' class with 'line' as an argument
# and store it in the variable 'gamep2'
gamep2 = Game(line)
# Initialize the variable 'drop' with the value of the third command-line argument
# If no third argument is provided, default to 1,000,000,000,000
drop = int(sys.argv[2]) if len(sys.argv) > 2 else 1_000_000_000_000

# Start an infinite loop
while True:
    # Call the 'drop1rock()' method on the 'gamep2' object
    # and store the return value in the variables 'pa' and 'po'
    pa, po = gamep2.drop1rock()
    # If 'pa' is a value that evaluates to 'True', break out of the loop
    if pa:
        break
# Initialize the variable 'rocks_left' with the value of 'drop' minus
# the value of the 'num' attribute of the 'gamep2' object plus 1
rocks_left = drop - gamep2.num + 1
# Initialize the variable 'fake_sections' with the result of integer division
# of 'rocks_left' by 'po'
fake = rocks_left // po
# Initialize the variable 'moredrops' with the result of 'rocks_left' minus
# the product of 'fake' and 'po'
moredrops = rocks_left - (fake* po)
# Iterate 'moredrops' times and call the 'drop_one_rock()' method on the 'gamep2' object
# on each iteration
for _ in range(moredrops):
    gamep2.drop1rock()

# Initialize the variable 'part2' with the value of 'gamep2.h' plus
# the product of 'fake_sections' and 'pa'

part2 = gamep2.h + (fake * pa)
# Print 'part2' to the console with the string 'Part 2: ' preceding it
print(f'Part 2: {part2}')