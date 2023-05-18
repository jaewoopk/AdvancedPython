# list = []

# n = int(input())

# for i in range(n) :
#     list.append(int(input()))

# max = -2100000000
# for i in range(n - 1) :
#     for j in range(i + 1, n) :
#         if (list[i] + list[j] > max) :
#             max = list[i] + list[j]

# print(max)


list = []
n = int(input())

real_sum = 0
fake_sum = 0

for i in range(n) :
    list.append(int(input()))

minValue = min(list)

for i in range(n) :
    real_sum += list[i]
    fake_sum += (minValue / list[i]) * 100

print("%.02f"%(real_sum / n))
print("%.02f"%(fake_sum / n))