# # total = 0

# # while (True) :
# #     color = input()
# #     if (color == 'white') :
# #         total += 1000
# #     elif (color == 'yellow') :
# #         total += 2000
# #     elif (color == 'blue') :
# #         total += 3000
# #     elif (color == 'red') :
# #         total += 5000
# #     else :
# #         break

# # print("Total price = %d"%total)

# n = int(input())

# sw_list = []
# os_list = []
# db_list = []

# for i in range(n) :
#     sw, os, db = input().split()
#     sw_list.append(int(sw))
#     os_list.append(int(os))
#     db_list.append(int(db))

# print("Average(SW) = %d"%(int(sum(sw_list) / n)))
# print("Average(OS) = %d"%(int(sum(os_list) / n)))
# print("Average(DB) = %d"%(int(sum(db_list) / n)))



# total = 0

# n = int(input())

# for i in range(n) :
#     rice = input()
#     if (rice == 'salmon roe') :
#         total += 1000
#     elif (rice == 'red sea bream') :
#         total += 3000
#     elif (rice == 'egg roll') :
#         total += 1000
#     elif (rice == 'shrimp') :
#         total += 2000
#     elif (rice == 'kimbab') :
#         total += 1000
#     elif (rice == 'tuna') :
#         total += 5000
#     else :
#         continue

# print("Total price = %d"%total)

# list = []
# for i in range(8) :
#     list.append(int(input()))

# list.sort(reverse=True)

# for i in list :
#     print(i)

def avg(list) :
    total = 0
    hakjum = [3,3,3,2,1]
    for i in range(5) :
        if (list[i] == 'A') :
            total += (hakjum[i] * 4.0)
        elif (list[i] == 'B') :
            total += (hakjum[i] * 3.0)
        elif (list[i] == 'C') :
            total += (hakjum[i] * 2.0)
        elif (list[i] == 'D') :
            total += (hakjum[i] * 1.0)
    return total / 12

Grade = [
['C', 'B', 'A', 'C', 'D'],
['F', 'D', 'C', 'D', 'B'],
['A', 'B', 'A', 'B', 'A'],
['A', 'A', 'B', 'C', 'D'],
['B', 'B', 'B', 'B', 'B'],
['B', 'B', 'C', 'D', 'F'],
['C', 'A', 'A', 'A', 'A'],
['D', 'A', 'A', 'C', 'F']
]

for i in range(1, 9) :
    print("%d %.2f"%(i,avg(Grade[i - 1])))