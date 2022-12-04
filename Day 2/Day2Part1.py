with open('inputDay2.txt') as f:
    lines = f.readlines()
print(lines)

opponentChoice = []
yourChoice = []
score = 0

for line in lines:
    opponentChoice.append(line[0])
    yourChoice.append(line[2])

for i in range(len(opponentChoice)):

    if yourChoice[i] == "X":
        #Rock
        score += 1
        choice = "A"
    elif yourChoice[i] == "Y":
        #Paper
        score += 2
        choice = "B"
    elif yourChoice[i] == "Z":
        #Scissors
        score += 3
        choice = "C"

    if choice == opponentChoice[i]:
        score += 3
    elif choice == "B" and opponentChoice[i] == "A":
        #Win
        score += 6
    elif choice == "C" and opponentChoice[i] == "B":
        #Win
        score += 6
    elif choice == "A" and opponentChoice[i] == "C":
        #Win
        score += 6


print(opponentChoice)
print(yourChoice)
print(score)