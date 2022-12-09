with open('InputDay9.txt') as f:
    lines = f.readlines()

class Item:
  def __init__(self):
    self.x = 0
    self.y = 0
    self.history = [(0,0)]

head = Item()
tail = Item()

def updateTail():
    diff = abs(head.x - tail.x)+abs(head.y - tail.y)
    if diff > 1:
        if abs(head.x-tail.x) != 1 or abs(head.y-tail.y) != 1:
            if (head.x - tail.x == 1 and head.y - tail.y == 2) or (head.x - tail.x == 2 and head.y - tail.y == 1):
                #bottomLeft
                tail.x+= 1
                tail.y+= 1
            elif (head.x - tail.x == -1 and head.y - tail.y == 2) or (head.x - tail.x == -2 and head.y - tail.y == 1):
                #Bottomright
                tail.x -= 1
                tail.y += 1
            elif (head.x - tail.x == -1 and head.y - tail.y == -2) or (head.x - tail.x == -2 and head.y - tail.y == -1):
                #TopRight
                tail.x -= 1
                tail.y -= 1
            elif (head.x - tail.x == 1 and head.y - tail.y == -2) or (head.x - tail.x == 2 and head.y - tail.y == -1):
                #TopLeft
                tail.x += 1
                tail.y -= 1
            elif head.x - tail.x == 2:
                tail.x+= 1
            elif head.x - tail.x == -2:
                tail.x -= 1
            elif head.y - tail.y == 2:
                tail.y+= 1
            elif head.y - tail.y == -2:
                tail.y -= 1





for line in lines:
    if "\n" in line:
        line = line.strip('\n')
    split = line.split(" ")
    direction = split[0]
    amount = int(split[1])
    for i in range(amount):
        if direction == "R":
            head.x += 1
        elif direction == "L":
            head.x -= 1
        elif direction == "U":
            head.y += 1
        elif direction == "D":
            head.y -= 1
        updateTail()
        head.history.append((head.x, head.y))
        tail.history.append((tail.x, tail.y))

print("There are "+str(len(list(dict.fromkeys(tail.history)))) +" position the tail was at.")