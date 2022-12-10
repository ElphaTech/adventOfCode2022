file = open("Day 3/input.txt", "r")

pri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
t = 0

for line in file:
    line = line.strip()
    line = [line[:int(len(line)/2)],line[int(len(line)/2):]]
    for l in line[0]:
        if l in line[1]:
            t += pri.find(l)+1
            break
print(t)