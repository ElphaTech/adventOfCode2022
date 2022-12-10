file = open("Day 4/input.txt", "r")

t = 0

for line in file:
    line = line.strip()
    templ = line
    line = line.split(',')
    firstStart,firstEnd = line[0].split('-')
    secondStart,secondEnd = line[1].split('-')
    firstStart,firstEnd,secondStart,secondEnd = int(firstStart),int(firstEnd),int(secondStart),int(secondEnd)

    if firstStart <= secondStart and firstEnd >= secondEnd:
        t += 1
    elif firstStart >= secondStart and firstEnd <= secondEnd:
        t += 1

print(t)