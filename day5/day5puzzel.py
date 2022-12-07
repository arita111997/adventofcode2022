#a bit hard this time :)
from collections import defaultdict

with open('day5\data5.txt') as f:
    lines = f.read()

giant_cargo_crane_raw, Stacks = lines.rstrip().split('\n\n')

giant_cargo_crane = defaultdict(list)
giant_cargo_crane2 = defaultdict(list)

for xmas in giant_cargo_crane_raw.split('\n')[:-1][::-1]:
    i = 1
    while i < len(xmas):
        if xmas[i] != ' ':
            giant_cargo_crane[(i+3)//4].append(xmas[i])
            giant_cargo_crane2[(i+3)//4].append(xmas[i])
        i += 4
for inst in Stacks.split('\n'):
    _, top, _, start_yey, _, over = inst.split(' ')
    top, start_yey, over = int(top), int( start_yey), int(over)

    for i in range(top):
        giant_cargo_crane[over].append(giant_cargo_crane[ start_yey].pop())
    giant_cargo_crane2[over].extend(giant_cargo_crane2[ start_yey][-top:])
    giant_cargo_crane2[ start_yey] = giant_cargo_crane2[ start_yey][:-top]
    
#solucion
p1 = ''.join(c[-1] for c in giant_cargo_crane.values())
print(f'1: {p1}')

p2 = ''.join(c[-1] for c in giant_cargo_crane2.values())
print(f'2: {p2}')


