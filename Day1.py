# result = 0

# result += 1
# result += 2
# result += 3
# result += 4
# result += 5

# print("Result = %d"%(result))


# n1 = int(input())
# n2 = int(input())

# tmp = n1
# n1 = n2
# n2 = tmp

# print("n1 = %d"%(n1))
# print("n2 = %d"%(n2))


# value = int(input())

# print("before = %d"%(value))
# print("after = %d"%(value * 0.9))


# a = input()
# num = int(input())

# print("Result = ",end='')

# for i in range(num) :
#     print("%s"%(a),end='')

# n = int(input())

# print("x %d"%(n))

# for i in range(1, 10) :
#     print("%d x %d = %d"%(n,i,n * i))


second = int(input())

d = (int)(second / (24 * 3600))
h = (int)(second / 3600 - (24 * d))
m = (int)((second / 60) % 60)
s = second % 60

print("%d days %02d:%02d:%02d"%(d,h,m,s))
