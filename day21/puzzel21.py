from sympy import symbols, solve, simplify

def ex(s):
    """Recursively evaluates and simplifies the expression in string 's'"""
    if s.isnumeric() or s == 'x': return s
    tk = s.split()
    # Recursively evaluate and simplify the subexpressions
    return '(' + ex(dict[tk[0]]) + ' ' + tk[1] + ' ' + ex(dict[tk[2]]) + ')'

# Read and parse the data from the input file
with open(r"adventofcode\day21\data21.yaml") as f:
    dict = {l[:4]: l[6:] for l in f.read().splitlines()}

# Part 1: Simplify the root expression
print ("Part 1:", simplify(ex(dict['root'])))

# Part 2: Substitute the human expression with 'x' and solve for 'x'
dict['humn'] = 'x'
s = dict['root'].split()
dict['root'] = s[0] + ' - ' + s[2]
print ("Part 2:", solve(ex(dict['root']), symbols('x'))[0])
