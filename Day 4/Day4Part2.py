import time
startTime = time.time()

with open('inputDay4.txt') as f:
    lines = f.readlines()
#print(lines)
#print(lines[0].split(","))

bigBuddy = []
smallBuddy = []


def getRange(input):
    x = int(input.split("-")[0])
    y = int(input.split("-")[1])
    if x > y:
        sol = x-y
    else:
        sol = y-x
    return sol


#split into 2 parallel arrays
for line in lines:
    if '\n' in line:
        line = line.strip('\n')
    left = line.split(",")[0]
    right = line.split(",")[1]
    leftRange = getRange(left)
    rightRange = getRange(right)
    if leftRange > rightRange:
        bigBuddy.append(left)
        smallBuddy.append(right)
    else:
        bigBuddy.append(right)
        smallBuddy.append(left)

counter = 0

for i in range(len(bigBuddy)):
    bigBottom = int(bigBuddy[i].split("-")[0])
    bigTop = int(bigBuddy[i].split("-")[1])
    smallBottom = int(smallBuddy[i].split("-")[0])
    smallTop = int(smallBuddy[i].split("-")[1])
    if smallTop <= bigTop and smallTop >= bigBottom:
        counter += 1
    elif smallBottom <= bigTop and smallBottom >= bigBottom:
        counter += 1


print(counter)

end = time.time()
print(f"Total runtime of the program is {end - startTime}")