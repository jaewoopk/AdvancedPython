n = int(input())
m = int(input())

drink = [[]] * n
snack = [[]] * m
for i in range(n):
    drink[i] = [0]*n

for i in range(m) :
    snack[i] = [0]*m

while (True) :
    str = input()
    if (str[0] != 'd' and str[0] != 's' and str[0] != 'n') :
        print("Wrong Input")
        continue
    if (str[0] == 'n') :
        break
    if (str[0] =='d' and len(str) == 4) :
        drink[(int)(str[1])][(int)(str[2])] = int(str[3])
    elif (str[0] =='s' and len(str) == 4) :
        snack[(int)(str[1])][(int)(str[2])] = int(str[3])
    elif (str[0] =='d' and len(str) == 5) :
        drink[(int)(str[1])][(int)(str[2])] = int(str[3]) * 10 + int(str[4])
    elif (str[0] =='s' and len(str) == 5) :
        snack[(int)(str[1])][(int)(str[2])] = int(str[3]) * 10 + int(str[4])

print(drink)
print(snack)

