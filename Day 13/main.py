file = open("Day 13/example.txt", "r")

curL = 'l'
data = []

def makeList(inp):
    if inp.count('[') == 1:
        print(inp)
        return list((inp[1,-1]).split(','))
    else:
        openC = 0
        closeC = 0
        commas = [0]
        for char in range(len(inp)):
            if inp[char] == '[':
                openC += 1
            elif inp[char] == ']':
                closeC += 1
            elif inp[char] == ',' and openC == closeC:
                commas.append(char)
        commas.append(-1)
        tmpL = []
        for c in range(len(commas)-1):
            tmpL.append(inp[commas[c]:commas[c+1]])
        print(tmpL)
        return makeList(tmpL)

for line in file:
    line = line.strip()
    if line != '':
        line = makeList(line)
        print(line)
        if curL == 'l':
            data.append({})
            data[-1]['left'] = line
            curL = 'r'
        elif curL == 'r':
            data[-1]['right'] = line
            curL = 'l'

# def checkOrder(lInp,rInp):
#     if lInp == '' or rInp == '':
#         return False
#     elif lInp[0] == '[' and rInp[0] == '[':
#         if 



# inOrder = 0
# for pair in range(len(data)):
#     if checkOrder(data[pair]['left'],data[pair]['right']):
#         inOrder += 1
