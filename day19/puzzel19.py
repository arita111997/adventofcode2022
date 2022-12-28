import re
import collections
import math
# Constants representing each robot
oR, cL, oB, gE = 1, 2, 3, 4
# List of all robots
ms= [oR, cL, oB, gE]

def pbt(s):
    """Parses a string and returns a dictionary representing the production
        costs and requirements for each robot """
    l = list(map(int, re.findall("\d+", s)))
    return {
        oR: {oR: l[1]},
        cL: {oR: l[2]},
        oB: {oR: l[3], cL: l[4]},
        gE: {oR: l[5], oB: l[6]}
    }

def gmr(po):
    """Calculates the maximum number of each robot that can be produced given
        the production costs and requirements in the dictionary 'po'"""
    mr = {m: 0 for m in ms}
    mr[gE] = 100
    for _, needs in po.items():
        for robot, qty in needs.items():
            mr[robot] = max(mr[robot], qty)
    return mr

def gbo(po, assets):
    """Calculates the robots that can be built based on the resources available
    in the dictionary 'assets' and the production costs and requirements in
    the dictionary 'po'"""
    options = {0} # Option to skip building a robot
    for robot, needs in po.items():
        if all(qty <= assets[need] for need, qty in needs.items()):
            options.add(robot)
    if gE in options:
        return {gE}
    return options

def br(po, robots, assets, tb):
    """Builds a robot 'tb' given the production costs and requirements in the
    dictionary 'po', the current number of robots in the dictionary 'robots',
    and the resources available in the dictionary 'assets'"""
    robots[tb] += 1
    for resource, qty in po[tb].items():
        assets[resource] -= qty
        assert assets[resource] >= 0
    return (robots, assets)

def crop(robots, assets):
    """Calculates the resources gained from selling the robots in the dictionary
    'robots'"""
    for k, v in robots.items():
        assets[k] += v
    return assets

def lpo(po, e_time):
    """Calculates the maximum amount of gold obtained by building robots given
    the production costs and requirements in the dictionary 'po' until the
    elapsed time 'e_time'"""
    ir = {m: 0 for m in ms}  # Initial number of robot
    ir[oR] = 1
    kneel = [(0, ir, {m: 0 for m in ms}, set())]  # Initial stat
    b_time = collections.defaultdict(int) # Maximum gold obtained at each time
    mr = gmr(po) # Maximum number of each robot that can be produced
    while kneel:
        t, robots, assets, skipped = kneel.pop(0)
        b_time[t] = max(b_time[t], assets[gE])  # Update maximum gold
        if t <= e_time and b_time[t] == assets[gE]:
            options = gbo(po, assets) # Calculate build options
            for tb in options:
                if not tb:  # Skip building a robot
                    assets1 = crop(robots, assets.copy())
                    kneel.append((t + 1, robots, assets1, options))
                elif tb in skipped: # Skip building a robot that has already been skipped
                    continue
                elif robots[tb] + 1 > mr[tb]: # Skip building more robots than the maximum
                    continue
                else:
                    robots1, assets1 = br(
                        po, robots.copy(), assets.copy(), tb)
                    assets1 = crop(robots, assets1.copy())
                    kneel.insert(0, (t + 1, robots1, assets1, set()))
    return b_time[e_time]

# Read production costs and requirements from file
pos = list(map(pbt, open('adventofcode\day19\data19.txt').read().split('\n')))
# Part 1: Calculate total gold obtained from building robots in all time periods
print(sum((i + 1) * lpo(po, 24) for i, po in enumerate(pos)))
# Part 2: Calculate gold obtained from building robots in the first 3 time periods
print(math.prod(lpo(po, 32) for po in pos[:3]))
