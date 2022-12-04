with open('inputDay1.txt') as f:
    lines = f.readlines()
print(lines)

import numpy as np

addedUp = []
counter = 0
for i in lines:
    if '\n' in i:
        i = i.strip('\n')
        print("asdfasdfdsasdd")
    print(i)
    #print("asdf")
    if i == "":
        addedUp.append(counter)
        counter = 0
    else:
        counter = counter+int(i)


print(np.max(addedUp))
#print(addedUp)