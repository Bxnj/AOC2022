with open('inputDay1.txt') as f:
    lines = f.readlines()
print(lines)

import numpy as np

addedUp = []
counter = 0
for i in lines:
    i = i.strip('\n')
    #print(i)
    #print("asdf")
    if i == "":
        addedUp.append(counter)
        counter = 0
    else:
        counter = counter+int(i)

addedUp.append(counter)

print(addedUp)
print(list(reversed(sorted(addedUp))))
print(list(reversed(sorted(addedUp)))[0]+list(reversed(sorted(addedUp)))[1]+list(reversed(sorted(addedUp)))[2])
#print(addedUp)


#203194