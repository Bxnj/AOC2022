with open('InputDay9.txt') as f:
    lines = f.readlines()

knots=[]

class Item:
  def __init__(self,prev):
    self.previous = prev
    self.x = 0
    self.y = 0
    self.history = [(0,0)]
    knots.append(self)

  def updateKnot(self):
      diff = abs(self.previous.x - self.x) + abs(self.previous.y - self.y)
      if diff > 1:
          if abs(self.previous.x - self.x) != 1 or abs(self.previous.y - self.y) != 1:
              if (self.previous.x - self.x == 1 and self.previous.y - self.y == 2) or (
                      self.previous.x - self.x == 2 and self.previous.y - self.y == 1) or (
                      self.previous.x - self.x == 2 and self.previous.y - self.y == 2):
                  # bottomLeft
                  self.x += 1
                  self.y += 1
              elif (self.previous.x - self.x == -1 and self.previous.y - self.y == 2) or (
                      self.previous.x - self.x == -2 and self.previous.y - self.y == 1) or (
                      self.previous.x - self.x == -2 and self.previous.y - self.y == 2):
                  # Bottomright
                  self.x -= 1
                  self.y += 1
              elif (self.previous.x - self.x == -1 and self.previous.y - self.y == -2) or (
                      self.previous.x - self.x == -2 and self.previous.y - self.y == -1) or (
                      self.previous.x - self.x == -2 and self.previous.y - self.y == -2):
                  # TopRight
                  self.x -= 1
                  self.y -= 1
              elif (self.previous.x - self.x == 1 and self.previous.y - self.y == -2) or (
                      self.previous.x - self.x == 2 and self.previous.y - self.y == -1) or (
                      self.previous.x - self.x == 2 and self.previous.y - self.y == -2):
                  # TopLeft
                  self.x += 1
                  self.y -= 1
              elif self.previous.x - self.x == 2:
                  self.x += 1
              elif self.previous.x - self.x == -2:
                  self.x -= 1
              elif self.previous.y - self.y == 2:
                  self.y += 1
              elif self.previous.y - self.y == -2:
                  self.y -= 1

head = Item(None)
one = Item(head)
two = Item(one)
three = Item(two)
four = Item(three)
five = Item(four)
six = Item(five)
seven = Item(six)
eight = Item(seven)
nine = Item(eight)







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

        for knot in knots:
            if knot != head:
                knot.updateKnot()
                knot.history.append((knot.x, knot.y))



print("There are "+str(len(list(dict.fromkeys(nine.history)))) +" positions the tail was at.")