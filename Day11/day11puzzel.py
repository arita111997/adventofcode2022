class Monkey_in_the_Middle:
    def __init__(self, monkey_xmas):
        stats = monkey_xmas.splitlines()
        self.i = eval('[' + stats[1][18:] + ']')
        self.o = eval('lambda old: ' + stats[2][19:])
        self.test = int(stats[3][21:])
        self.true = int(stats[4][29:])
        self.false = int(stats[5][30:])
        self.inspect_monkeys = 0
    
    def run(self, worry_or_not):
        while self.i:
            self.inspect_monkeys += 1
            omg = self.o(self.i.pop(0))
            omg = omg % 9699690 if worry_or_not == 1 else omg // worry_or_not
            yield self.false if omg % self.test else self.true, omg

def xmas_game(rounds, worry_or_not):
    with open(r'Day11\data11.txt') as f:
        santa_monkeys = [Monkey_in_the_Middle(monkey_xmas) for monkey_xmas in f.read().split('\n\n')]

    for _ in range(rounds):
        for monkey_xmas in santa_monkeys:
            for catcher, omg in monkey_xmas.run(worry_or_not):
                santa_monkeys[catcher].i.append(omg)

    return (lambda x, y: x.inspect_monkeys * y.inspect_monkeys) \
        (*sorted(santa_monkeys, key=lambda monkey_xmas: monkey_xmas.inspect_monkeys)[-2:])


print("Part 1:",xmas_game(20, 3))
 
print("Part 2:", xmas_game(10000, 1))