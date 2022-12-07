def Trouble1():
    f = open('day 6\data6.txt')
    data = f.readline().strip()
    for i in range(len(data)):
        if len(set(data[i:i + 4])) == 4:
            return i + 4


def Trouble2():
    f = open('day 6\data6.txt')
    data = f.readline().strip()
    for i in range(len(data)):
        if len(set(data[i:i + 14])) == 14:
            return i + 14

print(Trouble1())
print(Trouble2())