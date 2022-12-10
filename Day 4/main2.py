file = open("Day 4/input.txt", "r")

t = 0

for line in file:
    line = line.strip()
    templ = line
    line = line.split(',')
    firstStart,firstEnd = line[0].split('-')
    secondStart,secondEnd = line[1].split('-')
    firstStart,firstEnd,secondStart,secondEnd = int(firstStart),int(firstEnd),int(secondStart),int(secondEnd)

    dbreak = False
    for i in range(firstStart,firstEnd+1):
        for j in range(secondStart,secondEnd+1):
            if i == j:
                t += 1
                dbreak = True
                break
        if dbreak:
            break

print(t)