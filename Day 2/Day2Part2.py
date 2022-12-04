with open('inputDay2.txt') as f:
    lines = f.readlines()
print(lines)

opponentChoice = []
desiredOutcome = []
score = 0

for line in lines:
    opponentChoice.append(line[0])
    desiredOutcome.append(line[2])

for i in range(len(opponentChoice)):

    if desiredOutcome[i] == "X":
        #Loose
        choice = "L"
    elif desiredOutcome[i] == "Y":
        #Draw
        score += 3
        choice = "D"
    elif desiredOutcome[i] == "Z":
        #Win
        score += 6
        choice = "W"

    if choice == "D":
        if opponentChoice[i] == "A":
            # Rock
            score += 1
        elif opponentChoice[i] == "B":
            # Paper
            score += 2
        elif opponentChoice[i] == "C":
            # Scissors
            score += 3
    if choice == "L":
        if opponentChoice[i] == "A":
            # Rock
            score += 3
        elif opponentChoice[i] == "B":
            # Paper
            score += 1
        elif opponentChoice[i] == "C":
            # Scissors
            score += 2
    if choice == "W":
        if opponentChoice[i] == "A":
            # Rock
            score += 2
        elif opponentChoice[i] == "B":
            # Paper
            score += 3
        elif opponentChoice[i] == "C":
            # Scissors
            score += 1


print(opponentChoice)
#print(yourChoice)
print(score)