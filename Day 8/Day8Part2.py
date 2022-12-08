with open('InputDay8.txt') as f:
    lines = f.readlines()

totalArray = []

for line in lines:
    if "\n" in line:
        line = line.strip('\n')
    tempArray = []
    for char in line:
        tempArray.append(int(char))
    totalArray.append(tempArray)

print(totalArray)

def checkTopandBottomDistance(x,y, height):
    distanceTop = 0
    distanceBottom = 0
    initialY = y
    while y > 0:
        y -= 1
        if totalArray[y][x] >= height:
            distanceBottom+=1
            break
        else:
            distanceBottom+=1
    y = initialY
    while y < len(totalArray)-1:
        y+=1
        if totalArray[y][x] >= height:
            distanceTop+=1
            break
        else:
            distanceTop += 1
    return (distanceBottom, distanceTop)

def checkLeftandRightDistance(x,y, height):
    distanceRight = 0
    distanceLeft = 0
    initialX = x
    while x > 0:
        x -= 1
        if totalArray[y][x] >= height:
            distanceLeft += 1
            break
        else:
            distanceLeft+=1
    x = initialX
    while x < len(totalArray[0])-1:
        x+=1
        if totalArray[y][x] >= height:
            distanceRight += 1
            break
        else:
            distanceRight += 1
    return (distanceLeft, distanceRight)

max = 0
for x in range(len(totalArray[0])):
    for y in range(len(totalArray)):
        if x != 0 and y != 0 and x != len(totalArray[0])-1 and y != len(totalArray)-1:
            bottomTop = checkTopandBottomDistance(x, y, totalArray[y][x])
            leftRight = checkLeftandRightDistance(x, y, totalArray[y][x])
            total = bottomTop[1] * bottomTop[0] * leftRight[0] * leftRight[1]
            if total > max:
                max = total
print("This is the max scenic score: " + str(max))