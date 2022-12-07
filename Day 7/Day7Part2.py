#import sys
#sys.setrecursionlimit(3000)
with open('InputDay7.txt') as f:
    lines = f.readlines()
print(lines)
lines.append("STOPPER")

directoryList = []
sum = 0
sublist = []
currentPath = ""

class Directory:
  def __init__(self, name, size, sublist, path):
    self.name = name
    self.size = size
    self.sublist = sublist
    self.totalSize = 0
    self.path = path


def removeChars(string, n):
    string = string[:len(string) - n]
    return string

#parsing
for i in range(len(lines)):
    line=lines[i]
    if '\n' in line:
        line = line.strip('\n')
    print(line)
    if line == "$ cd /":
        currentPath = "/"
    elif line == "$ cd ..":
        currentPathSplit = currentPath.split("/")
        while ("" in currentPathSplit):
            currentPathSplit.remove("")
        toRemove = len(currentPathSplit[-1])+1
        currentPath = currentPath[:len(currentPath)-toRemove]
    elif line[2] == "l" and line[0] == "$":
        for k in range(len(lines)-i-1):
            k += i+1
            if lines[k][0] == "$" or lines[k] == "STOPPER":
                currentPathSplit = currentPath.split("/")
                while ("" in currentPathSplit):
                    currentPathSplit.remove("")
                if currentPathSplit == []:
                    name="/"
                else:
                    name = currentPathSplit[-1]
                newDir = Directory(name, sum, sublist, currentPath)
                directoryList.append(newDir)
                sum = 0
                sublist = []
                break
            splitted = lines[k].split(" ")
            if splitted[0] == "dir":
                toAppend = splitted[1]
                if '\n' in toAppend:
                    toAppend = toAppend.strip('\n')
                sublist.append(toAppend)
            else:
                sum += int(splitted[0])
    elif line[2] == "c" and line[0] == "$":
        currentPath = currentPath+line.split(" ")[-1]+"/"



def findDirectory(name, overDir):
    for directory in directoryList:
        syntaxedDirPath = overDir.path+name+"/"
        if directory.name == name and directory.path == syntaxedDirPath:
            return directory
    return False



doneTotalSize = []
for directory in directoryList:
    if directory.sublist == []:
        directory.totalSize = directory.size
        doneTotalSize.append(directory.path)
print(doneTotalSize)

for i in range(10000):
    for directory in directoryList:
        if directory.totalSize == 0:
            check = True
            for subDir in directory.sublist:
                searchedDir = findDirectory(subDir, directory)
                if searchedDir == False:
                    check = False
                else:
                    if searchedDir.path not in doneTotalSize:
                        check = False
            if check == True:
                for subDirs in directory.sublist:
                    directory.totalSize += findDirectory(subDirs, directory).totalSize
                directory.totalSize += directory.size
                doneTotalSize.append(directory.path)


totalUsedSpace = directoryList[0].totalSize
totalSpace = 70000000
neededSpace = 30000000
freeSpace = totalSpace-totalUsedSpace
toDelete = neededSpace-freeSpace
print(toDelete)
minDiff = 1000000000

for directory in directoryList:
    if directory.totalSize >= toDelete:
        diff = directory.totalSize - toDelete
        if diff < minDiff:
            minDiff = diff
            smallestDir = directory

print(minDiff)
print(smallestDir.__dict__)








