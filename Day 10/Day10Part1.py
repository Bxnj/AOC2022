with open('InputDay10.txt') as f:
    lines = f.readlines()

var = 1

solList = []

cycle = 1

def cycleCheck(cycle, var):
    if cycle == 0 or (cycle-20) % 40 == 0:
        solList.append(cycle*var)

for line in lines:
    if "\n" in line:
        line = line.strip('\n')
    cycleCheck(cycle, var)
    if line == "noop":
        cycle += 1
    else:
        cycle += 1
        cycleCheck(cycle, var)
        var += int(line.split(" ")[1])
        cycle += 1

total = 0
for sol in solList:
    total+=sol

print(total)
