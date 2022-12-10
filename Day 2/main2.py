file = open("Day 2/input.txt", "r")

tp = 0 #total points
lose = 'B A C B' #u lose
win = 'B C A B' #u win

for line in file:
    line = line.strip()

    line = line.replace('X','A')
    line = line.replace('Y','B')
    line = line.replace('Z','C')

    #lose,draw,win
    if line[2] == 'A':
        line = f"{line[0]} {lose[lose.find(line[0])+2]}"
    elif line[2] == 'B': #draw
        line = f"{line[0]} {line[0]}"
        tp += 3
    elif line[2] == 'C':
        line = f"{line[0]} {win[win.find(line[0])+2]}"
        tp += 6

    if line[2] == 'A':
        tp += 1
    elif line[2] == 'B':
        tp += 2
    elif line[2] == 'C':
        tp += 3


    print(f"-{line}-")
print(tp)