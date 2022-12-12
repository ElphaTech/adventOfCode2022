file = open("Day 7/input.txt", "r")

fileSystem = {}
curPos = [fileSystem]

for line in file:
    line = line.strip()
    if line[:4] == '$ cd':
        if line[-1] == '/':
            curPos = [fileSystem]
        elif line[-2:] == '..':
            curPos.pop()
        else:
            curPos.append(curPos[-1][line[5:]])

    elif line[:3] == 'dir':
        curPos[-1][line[4:]] = {}

    elif line[0].isdigit():
        sLine = line.split(' ')
        curPos[-1][sLine[1]] = int(sLine[0])


totalSize = 70000000

def countSize(folder):
    curFSize = 0
    for i in folder:
        if type(folder[i]) == int:
            curFSize += folder[i]
        elif type(folder[i]) == dict:
            curFSize += countSize(folder[i])
    global totalSize
    if curFSize > 1412830 and curFSize < totalSize:
        totalSize = curFSize
    return curFSize

# import json
# print(json.dumps(fileSystem))

print(countSize(fileSystem))
print(totalSize)