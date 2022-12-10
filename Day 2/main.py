file = open("Day 2/input.txt", "r")

tp = 0 #total points
beat = 'B A C B' #beats

for line in file:
    line = line.strip()

    line = line.replace('X','A')
    line = line.replace('Y','B')
    line = line.replace('Z','C')

    if line[0] == line[2]: #draw
        tp += 3
    elif line not in beat: #win
        tp += 6

    if line[2] == 'A':
        tp += 1
    elif line[2] == 'B':
        tp += 2
    elif line[2] == 'C':
        tp += 3


    print(f"-{line}-")
print(tp)