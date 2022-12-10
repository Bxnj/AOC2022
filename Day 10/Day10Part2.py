with open('InputDay10.txt') as f:
    lines = f.readlines()

var = 1
cycle = 1
subline = []
pic = []

def cycleCheck(cycle, var, subline):
    cycle -= 1
    if cycle >= 40:
        cycle = cycle%40
    if var == cycle or cycle == var-1 or cycle == var+1:
        subline.append("#")
    else:
        subline.append(".")



for line in lines:
    if "\n" in line:
        line = line.strip('\n')
    cycleCheck(cycle, var, subline)
    if cycle % 40 == 0:
        pic.append(subline)
        subline = []
    if line == "noop":
        cycle += 1
    else:
        cycle += 1
        cycleCheck(cycle, var, subline)
        if cycle %40 == 0:
            pic.append(subline)
            subline = []
        var += int(line.split(" ")[1])
        cycle += 1


finalString = ""
for line in pic:
    strline = ""
    for char in line:
        strline += char
    finalString += strline +"\n"
print(finalString)