myLocation = []
myX = int(input())
myY = int(input())
myLocation.append(myX)
myLocation.append(myY)

print(myLocation)

treasure = int(input())
treasureLocation = []
for i in range(treasure) :
    list = []
    list.append(int(input()))
    list.append(int(input()))
    treasureLocation.append(list)

print(treasureLocation)

moveCount = int(input())
treasureCount = 0
for i in range(moveCount) :
    moveX = int(input())
    moveY = int(input())
    x = moveX + myX
    y = moveY + myY
    list = [x,y]
    if (list in treasureLocation) :
        treasureCount += 1
    myX = x
    myY = y

print("%d!!"%treasureCount)


# 3
# 1
# 4
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 3
# 0
# 3
# 3
# 4
# -1
# -2