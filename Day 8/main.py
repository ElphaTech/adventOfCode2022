file = open("Day 8/input.txt", "r")

trees = []

for line in file:
    line = line.strip()
    trees.append(line)

totalVisible = len(trees)*2 + len(trees[0])*2-4

for row in range(1,len(trees)-1):
    for tree in range(1,len(trees[row])-1):
        height = int(trees[row][tree])

        lineBlock = False
        for xTree in range(tree): #w -> tree
            if int(trees[row][xTree]) >= height:
                lineBlock = True
        if lineBlock:
            lineBlock = False
            for xTree in range(tree+1,len(trees)): #tree -> e
                if int(trees[row][xTree]) >= height:
                    lineBlock = True
            if lineBlock:
                lineBlock = False
                for yTree in range(row): #n \/ tree
                    if int(trees[yTree][tree]) >= height:#north
                        lineBlock = True
                if lineBlock:
                    lineBlock = False
                    for yTree in range(row+1,len(trees[row])): #tree /\ s
                        if int(trees[yTree][tree]) >= height:#north
                            lineBlock = True
                    if not lineBlock:
                        totalVisible += 1
                else:
                    totalVisible += 1
            else:
                totalVisible += 1
        else:
            totalVisible += 1

print(totalVisible)