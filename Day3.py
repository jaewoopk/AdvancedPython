# name = input()
# residence = input()
# year = int(input())

# print("Name : %s"%name)
# print("Residence : %s"%residence)
# print("Birth Year : %d"%(2023 - year + 1))


# m = int(input())

# km = m / 1000
# mile = m / 1609
# inch = m * 39.37
# feet = m * 3.281

# print("%d m to km = %.2f km"%(m, km))
# print("%d m to mile = %.2f mile"%(m, mile))
# print("%d m to inch = %.2f inch"%(m, inch))
# print("%d m to feet = %.2f feet"%(m, feet))

# n = int(input())
# m = int(input())

# realM = (m // 10) + (m % 10)

# print("Result = %d"%(n * realM))


# ch = input()
# n = int(input())

# print("String = ",end='')
# for i in range(n) :
#     print(ch,end='')

# count = 0
# sum = 0

# while (1) :
#     n = int(input())
#     sum += n
#     count += 1
#     if (n == 4) :
#         break

# print("Count = %d, Total = %d"%(count, sum))


# n = int(input())

# x = 1
# i = 1
# while (n > x) :
#     i += 1
#     x *= i

# print("Num = %d"%(i))
# print("Total = %d"%(x))

count = 0
sum = 0

while (1) :
    n = int(input())
    count += 1
    if (n != 4) :
        sum += n
    else :
        break
    if (sum >= 20) :
        break

print("Count = %d\nTotal = %d"%(count, sum))