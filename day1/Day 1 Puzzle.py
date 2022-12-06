#part 1
print(max(sum(map(int,x.split()))for x in open('day1\calories.txt').read().split('\n\n')))
#part2
print(sum(sorted(sum(map(int,x.split()))for x in open('day1\calories.txt').read().split('\n\n'))[-3:]))