RPS = Rock, Paper, Scissors = "RPS"
LDW = Lose, Draw, Win = "LDW"
shape = dict(zip("ABCXYZ", (*RPS, *RPS)))
scoring = dict(zip(RPS, (1, 2, 3)))
win_scoring = dict(zip(LDW, (0, 3, 6)))

# game[(a, b)] is the result of the game from `b` point of view 
game = dict()
for a in RPS:
    game[(a, a)] = Draw
for a, b in ((Rock, Scissors), (Scissors, Paper), (Paper, Rock)):
    game[(a, b)] = Lose
    game[(b, a)] = Win

# shape_play[(a, res)] is the action to perform against `a` to get`res`
shape_play = {(a, res): b for (a, b), res in game.items()}


def score1(opponent, me) -> int:
    return win_scoring[game[opponent, me]] + scoring[me]

def elfgame(g):
    return sum(score1(shape[op], shape[me]) for op, me in g)

def score2(opponent, outcome):
    return win_scoring[outcome] + scoring[shape_play[opponent, outcome]]

def elfgame_2(g):
    outcomes = dict(zip("XYZ", LDW))
    return sum(score2(shape[op], outcomes[out]) for op, out in g)

# A g is a list of pair of strings
def get_g_from_str(string):
    return [tuple(l.strip().split(" ")) for l in string.splitlines()]

def get_g_from_file(file):
    with open(file) as f:
        return get_g_from_str(f.read())


# Unit-test 
g = get_g_from_str("""A Y
B X
C Z""")
assert elfgame(g) == 15
assert elfgame_2(g) == 12

# Actual problem
g= get_g_from_file("day2\data2.txt")
print(elfgame(g))
print(elfgame_2(g))