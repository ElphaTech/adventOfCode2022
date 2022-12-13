file = open("Day 8/input.txt", "r")

trees = []

for line in file:
    line = line.strip()
    trees.append(line)

highScenicS = 0

for row in range(len(trees)):
    for tree in range(len(trees[row])):
        height = int(trees[row][tree])

        tmpC = 1
        for xTree in range(tree,0,-1): #w <- tree
            if int(trees[row][xTree]) < height:
                tmpC += 1
            else:
                break
        wCount = tmpC
        tmpC = 1

        for xTree in range(tree+1,len(trees)): #tree -> e
            if int(trees[row][xTree]) < height:
                tmpC += 1
            else:
                break
        eCount = tmpC
        tmpC = 1

        for yTree in range(row,0,-1): #n \/ tree
            if int(trees[yTree][tree]) < height:
                tmpC += 1
            else:
                break
        nCount = tmpC
        tmpC = 1

        for yTree in range(row+1,len(trees[row])): #tree \/ s
            if int(trees[yTree][tree]) < height:
                tmpC += 1
            else:
                break
        sCount = tmpC

        scenicS = nCount*eCount*sCount*wCount
        if scenicS > highScenicS:
            highScenicS = scenicS

print(highScenicS)