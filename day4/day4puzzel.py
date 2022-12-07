def Camp_Cleanup(g,e):
    a, b = g.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))

    # check Camp_Cleanup 
    return e(a1 <= b1 <= a2, a1 <= b2 <= a2) or e(b1 <= a1 <= b2, b1 <= a2 <= b2)

with open("day4\data4.txt") as f:
    data4 = f.read().splitlines()

print ("1: ", len([x for x in data4 if Camp_Cleanup(x, lambda a,b: a and b)]))
print ("2: ", len([x for x in data4 if Camp_Cleanup(x, lambda a,b: a or b)]))
