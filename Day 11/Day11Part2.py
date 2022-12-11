with open('InputDay11.txt') as f:
    lines = f.readlines()



class Monkey:
  def __init__(self, name, startingItems, operation, test, targets):
    self.name = name
    self.items = startingItems
    self.operation = operation
    self.test = test
    self.targets = targets
    self.inspections = 0
  def processOperation(self, index):
      self.inspections += 1
      if self.operation[0] == "+":
          if self.operation[1] != "old":
              return self.items[index]+self.operation[1]
          elif self.operation[1] == "old":
              return self.items[index] + self.items[index]
      elif self.operation[0] == "*":
          if self.operation[1] != "old":
              return self.items[index]*self.operation[1]
          elif self.operation[1] == "old":
              return self.items[index] * self.items[index]

  def processTest(self, nr):
      if self.test[0] == "divisible":
          if nr % self.test[1] == 0:
              return True
          else:
              return False


rounds = 10000
allMonkeys = []





#Parse
for line in lines:
    if "\n" in line:
        line = line.strip('\n')
    splitted = line.split(" ")
    if len(splitted) >= 2:
        if splitted[0] == "Monkey":
            name = int(splitted[1].strip(":"))
        elif splitted[2] == "Starting":
            startingItems = []
            for i in range(len(splitted)-4):
                i+=4
                startingItems.append(int(splitted[i].strip(",")))
        elif splitted[2] == "Operation:":
            symbol = splitted[6]
            nr = splitted[7]
            if nr != "old":
                nr = int(nr)
            operation = (symbol, nr)
        elif splitted[2] == "Test:":
            test = (splitted[3], int(splitted[5]))
        elif splitted[4] == "If":
            if splitted[5] == "true:":
                targetTrue = int(splitted[-1])
            elif splitted[5] == "false:":
                targetFalse = int(splitted[-1])
                monkey = Monkey(name, startingItems, operation, test, (targetTrue, targetFalse))
                allMonkeys.append(monkey)

tempList = []
lcm = 1
#get LCM
for monkey in allMonkeys:
    tempList.append(monkey.test[1])
for item in tempList:
    lcm *= item


startTime = 0
for r in range(rounds):
    for monkey in allMonkeys:
        for i in range(len(monkey.items)):
            item = monkey.items[i]
            newWorryLvl = monkey.processOperation(i)
            while newWorryLvl > 1000000*lcm:
                newWorryLvl = newWorryLvl-(1000000*lcm)
            while newWorryLvl > 1000*lcm:
                newWorryLvl = newWorryLvl-(1000*lcm)
            while newWorryLvl > 10*lcm:
                newWorryLvl = newWorryLvl-(10*lcm)
            while newWorryLvl > lcm:
                newWorryLvl = newWorryLvl-lcm
            testResult = monkey.processTest(newWorryLvl)
            if testResult == True:
                target = monkey.targets[0]
            elif testResult == False:
                target = monkey.targets[1]
            for mon in allMonkeys:
                if mon.name == target:
                    mon.items.append(newWorryLvl)

        monkey.items = []

inspections = []

for monkey in allMonkeys:
    inspections.append(monkey.inspections)
    
inspections.sort()
inspections.reverse()

print("Monkey Buisness Level: " + str(inspections[0]*inspections[1]))