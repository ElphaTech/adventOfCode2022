file = open("1/act1", "r")

x = 0
l = []

for line in file:
    line = line.strip()
    if line == '':
        l.append(x)
        x = 0
    else:
        x += int(line)
if x != 0:
    l.append(x)

l.sort(reverse=True)
print(l[:3])
print(l[0]+l[1]+l[2])