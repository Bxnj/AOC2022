with open('inputDay6.txt') as f:
    lines = f.readlines()
input = lines[0]
#input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

for i in range(len(input)):
    if i+3 < len(input):
        print(input[i])
        if input[i] != input[i+1] and input[i] != input[i+2] and input[i] != input[i+3] and input[i+1] != input[i+2] and input[i+1] != input[i+3] and input[i+2] != input[i+3]:
            print(i+4)
            break