file = open("Day 3/input.txt", "r")

pri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = 0
tl = []

for line in file:
    tl.append(line.strip())
    if len(tl) == 3:
        for l in tl[0]:
            if l in tl[1] and l in tl[2]:
                t += pri.find(l)+1
                break
        tl = []
print(t)