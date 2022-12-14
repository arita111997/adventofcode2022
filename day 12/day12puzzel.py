from collections import deque

def Climbing(Hill, Elves):
    w, h = len(Hill[0]), len(Hill)
    xmas = deque([[Elves]])
    higher = set([Elves])
    while xmas:
        path = xmas.popleft()
        x, y = path[-1]
        if Hill[y][x] == "E":
            return path
        e = AB.index(Hill[y][x])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in higher:
                e2 = AB.index(Hill[y2][x2]) if Hill[y2][x2] != "E" else 26
                if e2 <= e + 1:
                    xmas.append(path + [(x2, y2)])
                    higher.add((x2, y2))

data = open("day 12\data12.txt").read().strip()
AB = "abcdefghijklmnopqrstuvwxyz"
Hill = [[c for c in line] for line in data.split("\n")]
y, x = [(n, r.index("S")) for n, r in enumerate(Hill) if "S" in r][0]
y2, x2 = [(n, r.index("E")) for n, r in enumerate(Hill) if "E" in r][0]
Hill[y][x] = "a"
starts = [(c, r) for r in range(len(Hill)) for c in range(len(Hill[0])) if Hill[r][c] == "a"]
hiking_trail = [len(Climbing(Hill, Elves)) - 1 for Elves in starts if Climbing(Hill, Elves)]


print(f"Part 1: {len(Climbing(Hill, (x, y))) - 1}")
print(f"Part 2: {min(hiking_trail)}")