#import
file = open("Day 5/input.txt", "r")

data = []
curL = 0

for line in file:
    line = line.replace('\n','')
    data.append(line)
    if line == '':
        blankL = curL
    curL += 1

columns = data[blankL-1].replace(' ','')

boxP = {}

for clm in columns:
    boxP[clm] = []
    for row in range(blankL-1):
        row = blankL - row -2
        acrP = int(clm)*4 - 3
        if data[row][acrP] != ' ':
            boxP[clm].append(data[row][acrP])

moves = data[blankL+1:]

#print boxes
def printB():
    for i in boxP:
        print(boxP[i])
    print()

#doing steps
for move in moves:
    boxes,mFrom,mTo = move.replace('move ','').replace(' from ',',').replace(' to ',',').split(',')
    boxes = int(boxes)

    for box in range(boxes):
        boxP[mTo].append(boxP[mFrom][-1])
        boxP[mFrom].pop(-1)
        # printB()

#print ans
ans = ''
for i in boxP:
    ans = f"{ans}{boxP[i][-1]}"
print(ans)