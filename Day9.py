# a = 0
# b = 0
# c = 0

# while True :
#     num = int(input())
#     if (num == 0) :
#         break
#     elif (num > 0) :
#         a += num

# tmp = a

# while True :
#     b += (tmp % 10)
#     c += 1
#     tmp //= 10
#     if (tmp == 0) :
#         break
#     b *= 10

# print(a+b+c)

# n = int(input())

# for i in range(n) :
#     ID = input()
#     age = int(input())
#     grade = input()
#     count = 0
#     for j in range(len(ID) - 1, -1, -1) :
#         if (ID[j] == '3') :
#             print("good",end='')
#             count += 1
#         elif (ID[j] == '6') :
#             print("luckGood",end='')
#             count += 10
#         elif (ID[j] == '9') :
#             print("boom",end='')
#             count += 100
#     if (count == 111) :
#         print('\nK',end='')
#     print()

n = int(input())

xCount = 0
starCount = 0

for i in range(n) :
    for j in range(n) :
        if (i == 0 or i == n - 1) :
            print("x",end='')
            xCount += 1
        elif (j == 0 or j == n - 1) :
            print("x",end='')
            xCount += 1
        elif (i == j or i == n - j - 1) :
            print("*",end='')
            starCount += 1
        else :
            print(" ",end='')
    print()

print("%d %d"%(xCount, starCount))