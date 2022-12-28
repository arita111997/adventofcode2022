def data():
    """Reads and returns the data from the input file as a list of tuples"""
    with open(r"adventofcode\day20\data20.txt") as f:
        return list(enumerate(map(int, f.read().splitlines())))

def zero(nl):
    """Returns the index of the tuple with a value of zero in the list 'nl'"""
    for x in range(len(nl)):
        if nl[x][1] == 0:
            return x

def xmas(count=1, ml=1):
    """Calculates and returns the sum of the values in the list after 'count'
    iterations, where each value is multiplied by 'ml' before the iterations"""
    nl = data()  # Initial list of tuples
    ls = len(nl)  # Length of the list

    # Multiply the values in the tuples by 'ml'
    nl = [(x, y * ml) for x, y in nl]

    for _ in range(count):  # Perform the iterations
        for x in range(ls):
            for z in range(ls):
                if nl[z][0] == x:  # Find the tuple with the current index
                    num = nl[z]  # Save the tuple
                    nl.pop(z)  # Remove the tuple from the list
                    if num[1] == -z:  # Special case: append the tuple to the end of the list
                        nl.append(num)
                    else:
                        # Insert the tuple at the new index calculated using its value
                        nl.insert((z + num[1]) % (ls-1), num)
                    break  # Break out of the inner loop

    ti = zero(nl)  # Find the index of the tuple with a value of zero
    # Calculate and return the sum of the values from the 1000th to the 4000th tuple
    return sum(nl[(ti + x) % len(nl)][1] for x in range(1000, 4000, 1000))

# Part 1: Calculate the sum of the values in the list after 1 iteration
print("Part 1:", xmas())

# Part 2: Calculate the sum of the values in the list after 10 iterations,
# where each value is multiplied by 811589153 before the iterations
print("Part 2:", xmas(10, 811589153))
