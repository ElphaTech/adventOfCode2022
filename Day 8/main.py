file = open("Day 8/example.txt", "r")

trees = []

for line in file:
    line = line.strip()
    trees.append(line)

totalVisible = len(trees)*2 + len(trees[0])*2-4

for x in range(1,len(trees)-1):
    for y in range(1,len(trees[x])-1):
        height = trees[x][y]

        for xs in range(len(trees[x])):
            if xs < x:#north
                pass
        for ys in range(len(trees)):
            pass