#part1
def Distress_Signal(l1, l2):
    if isinstance(l1, int) and isinstance(l2, int):
        if l1 == l2:
            return None
        return l1 < l2

    if isinstance(l1, list) and isinstance(l2, list):
        for e1, e2 in zip(l1, l2):
            if (comparison := Distress_Signal(e1, e2)) is not None:
                return comparison
        return Distress_Signal(len(l1), len(l2))

    if isinstance(l1, int):
        return Distress_Signal([l1], l2)
    return Distress_Signal(l1, [l2])

santa_text = open("day13\data13.txt", "r").read()
xmas_pairs = [[eval(l) for l in pair.splitlines()]for pair in santa_text.strip().split("\n\n")]
print(sum(i for i, (left, right) in enumerate(xmas_pairs, 1) if Distress_Signal(left, right)))


#part2
packets_right_order = [p for pair in xmas_pairs for p in pair]
p1 = 1 + sum(1 for p in packets_right_order if Distress_Signal(p, [[2]]))
p2 = 2 + sum(1 for p in packets_right_order if Distress_Signal(p, [[6]]))
print(p1 * p2)