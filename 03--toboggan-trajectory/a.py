import fileinput

pos = -3
trees = 0

for line in fileinput.input():
    line = line.strip()
    width = len(line)
    pos = (pos + 3) % width
    if line[pos] == '#':
        trees += 1

print(trees)
