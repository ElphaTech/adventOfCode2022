file = open("Day 6/input.txt", "r")

for line in file:
    line = line.strip()
    for pos in range(len(line)):
        tmp = []
        for let in line[pos:pos+14]:
            if let in tmp:
                break
            else:
                tmp.append(let)
        if len(tmp) == 14:
            print(pos+14)
            quit()
