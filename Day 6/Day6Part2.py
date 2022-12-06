with open('inputDay6.txt') as f:
    lines = f.readlines()
input = lines[0]
#input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

size = 14


def checkDuplicate(str):
    for i in range(len(str)):
        for k in range(len(str)):
            if i != k and str[i] == str[k]:
                return False
    return True


for i in range(len(input)):
    if i+size-1 < len(input):
        if checkDuplicate(input[i:i+size]) == True:
            print(i+size)
            break