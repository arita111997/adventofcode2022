from itertools import accumulate, zip_longest, starmap


# define a function to convert a character to a numerical value
# '=' is mapped to -2, '-' is mapped to -1, and all other characters are mapped to their integer values
xmas = lambda x: -2 if x == "=" else (-1 if x == "-" else int(x))

# read in the data from a file, split it into lines, and convert each line into a list of numerical values
smoothie  = [[xmas(ch) for ch in reversed(line)] for line in open('adventofcode\day25\data25.txt').read().split()]

# sum the values in each line to get the total value of each line
Hot = list(map(sum, (zip_longest(*smoothie , fillvalue=0))))

# use the accumulate function to apply the "compression" operation on the Hot list
# this operation takes the sum of the current and previous elements, divides it by 5, and stores the remainder
air = accumulate([0]+ Hot, lambda acc, el: (acc+el+2)//5)

# use the starmap function to apply the "decompression" operation on the zipped Hot and air lists
# this operation takes the sum of the current element of the Hot list and the previous element of the air list,
# divides it by 5, and stores the remainder
Hot = starmap(lambda a,b: ((a+b+2)%5)-2, zip(Hot, air))

# define a function to convert a numerical value to a character
# -2 is mapped to '=', -1 is mapped to '-', and all other values are mapped to their string representations
balloon = lambda x: "=" if x == -2 else ("-" if x == -1 else str(x))
# convert the Hot list into a list of characters and join them into a single string
output = "".join(reversed(list(map(balloon,Hot))))

# print the output string
print(output)