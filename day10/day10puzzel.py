def xmasrun(elf_commands):
    list = {'noop': (1, lambda x, _: x),
                   'addx': (2, lambda x, y: x + y)}
    x, clock_circuit = 1, 1
    state = [(0, 0)]

    for command in elf_commands:
        swim_elfs = command.split()
        santa = swim_elfs[0]
        xmas = int(swim_elfs[1]) if len(swim_elfs) == 2 else None
        x = list[santa][1](x, xmas)
        clock_circuit += list[santa][0]
        state.append((clock_circuit, x))

    return state


def elf_state_at(state, t):
    for i in range(len(state) - 1):
        if state[i][0] <= t < state[i + 1][0]:
            return state[i][1]
    return state[-1][1]


def cathode_Ray_Tube1(state: list):
    part1 = sum([elf_state_at(state, clock) *
                clock for clock in [20, 60, 100, 140, 180, 220]])
    print("Part 1: {}".format(part1))


def Sprite2(state: list):
    width, height = 40, 6
    xmassprite = [elf_state_at(state, pixel+1)
                  for pixel in range(width * height)]
    screen = ['#' if xmassprite[pixel]-1 <=
              (pixel % width) <= xmassprite[pixel]+1 else '.' for pixel in range(width * height)]

    print("Part 2:")
    
    for i in range(height):
        print(''.join(screen[i*width:(i+1)*width]))


with open(r"day10\data10.txt") as f:
    data = f.read().splitlines()

state = xmasrun(data)

cathode_Ray_Tube1(state)
Sprite2(state)