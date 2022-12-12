from math import sqrt

def Rope_Bridge (pz: list, rope: int) -> int:
    tail = [(0,0)] * rope
    map = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    tail_v = set()
    tail_v.add(tail[0])

    for command in pz:
        tail[-1] = (tail[-1][0] + command[1] * map[command[0]][0], tail[-1][1] + command[1] * map[command[0]][1])
        moved = True
        while moved:
            moved = False
            for i in range(len(tail) - 1, 0, -1):
                head = tail[i]
                tail_l = tail[i-1]
                dist_from_tail = sqrt((head[0] - tail_l[0]) ** 2 + (head[1] - tail_l[1]) ** 2)
                if dist_from_tail < 2.0: break
                tail_l = (tail_l[0] + step(head[0], tail_l[0]), tail_l[1] + step(head[1], tail_l[1]))
                moved = True
                tail[i-1] = tail_l
            tail_v.add(tail[0])
    
    return len(tail_v)

def gen(data: list):
    for l in data:
        t = l.split()
        yield t[0], int(t[1])

def step(a, b) -> int:
    return 0 if a == b else int(abs(a - b)/(a - b))

with open(r"day 9\data9.txt") as f:
    p = [command for command in gen(f.read().splitlines())]

print ("Part 1: {}".format(Rope_Bridge(p, 2)))
print ("Part 2: {}".format(Rope_Bridge(p, 10)))