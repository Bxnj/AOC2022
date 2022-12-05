with open('inputDay5.txt') as f:
    lines = f.readlines()

def createStartingGrid(lines):

    list = []


    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []


    for i in range(8):
        if(lines[i][1] != " "):
            list1.append(lines[i][1])
        if (lines[i][5] != " "):
            list2.append(lines[i][5])
        if (lines[i][9] != " "):
            list3.append(lines[i][9])
        if (lines[i][13] != " "):
            list4.append(lines[i][13])
        if (lines[i][17] != " "):
            list5.append(lines[i][17])
        if (lines[i][21] != " "):
            list6.append(lines[i][21])
        if (lines[i][25] != " "):
            list7.append(lines[i][25])
        if (len(lines[i])>=29 and lines[i][29] != " "):
            list8.append(lines[i][29])
        if (len(lines[i])>=33 and lines[i][33] != " "):
            list9.append(lines[i][33])
    list1.reverse()
    list2.reverse()
    list3.reverse()
    list4.reverse()
    list5.reverse()
    list6.reverse()
    list7.reverse()
    list8.reverse()
    list9.reverse()

    list.append(list1)
    list.append(list2)
    list.append(list3)
    list.append(list4)
    list.append(list5)
    list.append(list6)
    list.append(list7)
    list.append(list8)
    list.append(list9)
    print(list)
    return(list)


gridList = createStartingGrid(lines)

for i in range(len(lines)-10):
    i+=10
    amount = int(lines[i].split(" from ")[0].split(" ")[1])
    origin = int(lines[i].split(" from ")[1].split(" to ")[0])
    destination = int(lines[i].split(" from ")[1].split(" to ")[1])
    #print(str(amount)+" from " + str(origin)+ " to " + str( destination))
    for i in range(amount):
        toTransfer = gridList[origin-1][-1]
        gridList[destination-1].append(toTransfer)
        gridList[origin - 1].pop()
        print(toTransfer)
        print(i)

print(lines)
print(gridList)
