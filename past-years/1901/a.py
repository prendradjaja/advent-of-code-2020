import fileinput

answer = 0

def getfuel(mass):
    initfuel = mass // 3 - 2
    fuelfuel = initfuel // 3 - 2
    if fuelfuel <= 0:
        return initfuel
    else:
        return initfuel + getfuel(initfuel)

for line in fileinput.input():
    mass = int(line)
    answer += getfuel(mass)
print(answer)

# print(getfuel(14))
# print(getfuel(1969))
# print(getfuel(100756))
