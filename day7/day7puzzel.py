data7 = open("day7\data7.txt", "r", encoding="utf-8").read().splitlines()

xmas = [] 
The_device_the_of_Elves = []
for d in data7:
    a = d.strip().split()
    if a[0] == '$':
        if a[1] =='cd':
            if a[2] == '..':
                The_device_the_of_Elves.pop()
            else:
                if a[2] == '/': a[2]=''
                The_device_the_of_Elves.append(a[2] + '/')
    elif a[0] == 'dir':
        xmas.append([''.join(map(str,The_device_the_of_Elves)) + a[1] + '/', 0])
    else:
        xmas.append([''.join(map(str,The_device_the_of_Elves)) + a[1], int(a[0])])
 
xmas.sort()

sumy=0
bigsum=0
for a,b in xmas:
    if a[-1:]=='/': #directory
        for c,d in xmas:
            if c.find(a)!=-1: 
                sumy+=d
        if sumy<=100000:
            bigsum+=sumy
        sumy=0


sums=0
bigsums=[]
for a,b in xmas:
    if a[-1:]=='/': #directory
        for c,d in xmas:
            if c.find(a)!= -1: 
                sums+=d
        bigsums.append(sums)
        sums=0
 
bigsums.sort()
 
used = sum(b for a,b in xmas)
free = 70000000 - used
todelete = 30000000 - free
 
for d in bigsums:
    if d >= todelete:
        break


 #solucion
print('part1: ',bigsum)
print('part2: ',d)