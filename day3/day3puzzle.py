

def Rucksack(x):
    return ord(x) - ord('a') + 1 if x >= 'a' and x <= 'z' else ord(x) - ord('A') + 27

with open('day3\data3.txt') as f:
    data = f.read().splitlines()

#searching through a list of strings for the letter 
# that connects the string's two halves, figuring out its priority, and adding these.
part1 = sum(Rucksack(set(x[:len(x)//2]).intersection(set(x[len(x)//2:])).pop()) for x in data)
print (part1)

#This code creates a list of tuples with the following data: data[0], data[1], data[2], data[3], data[4], data[5],
# ..., with iter(data) adding new lines as needed and zip bringing everything back together.
part2 = sum(Rucksack(set(x[0]).intersection(set(x[1])).intersection(set(x[2])).pop()) \
    for x in zip(*[iter(data)]*3))
print (part2)