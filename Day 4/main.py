file = open("Day 4/input.txt", "r")

t = 0

for line in file:
    line = line.strip()
    line = line.split(',')
    line[0] = line[0].split('-')
    line[1] = line[1].split('-')

    if line[0][0] <= line[1][0] and line[0][1] >= line[1][1]:
        t += 1
    elif line[0][0] >= line[1][0] and line[0][1] <= line[1][1]:
        t += 1

print(t)