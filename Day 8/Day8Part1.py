with open('InputDay8.txt') as f:
    lines = f.readlines()
print(lines)

totalArray = []
counter = 0

for line in lines:
    if "\n" in line:
        line = line.strip('\n')
    tempArray = []
    for char in line:
        tempArray.append(int(char))
    totalArray.append(tempArray)

print(totalArray)

def checkLeftandRight(x,y, height):
    check1 = True
    check2 = True
    initialX = x
    while x > 0:
        x -= 1
        if totalArray[y][x] >= height:
            check1 = False
            break
    x = initialX
    while x < len(totalArray[0])-1:
        x+=1
        if totalArray[y][x] >= height:
            check2 = False
            break
    if check1 == True or check2 == True:
        return True
    else:
        return False




def checkTopandBottom(x,y, height):
    check1 = True
    check2 = True
    initialY = y
    while y > 0:
        y -= 1
        if totalArray[y][x] >= height:
            check1 = False
            break
    y = initialY
    while y < len(totalArray)-1:
        y+=1
        if totalArray[y][x] >= height:
            check2 = False
            break
    if check1 == True or check2 == True:
        return True
    else:
        return False



def checkCoords(x,y):
    height = totalArray[y][x]
    if checkLeftandRight(x,y,height) == True or checkTopandBottom(x,y,height) == True:
        return True

for x in range(len(totalArray[0])):
    for y in range(len(totalArray)):
        if x == 0 or y == 0 or x == len(totalArray[0])-1 or y == len(totalArray)-1:
            counter += 1
        else:
            if checkCoords(x,y) == True:
                counter += 1

print("There are exactly "+ str(counter) + " Trees visible from outside the grid")