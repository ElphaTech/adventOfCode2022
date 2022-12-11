file = open("Day 7/example.txt", "r")

fileSystem = {}
curPos = ['fileSystem']

for line in file:
    line = line.strip()
    if line[:4] == '$ cd':
        if line[-1] == '/':
            curPos = ['fileSystem']
        elif line[-2:] == '..':
            curPos.pop()
        else:
            curPos.append(f"{curPos[-1]}['{line[5:]}']")

    elif line[:3] == 'dir':
        eval(f"{curPos[-1]}['{line[4:]}'] = {'{}'}")

    elif line[0].isdigit():
        sLine = line.split(' ')
        eval(f"{curPos[-1]}['{line[4:]}'] = {'{}'}")