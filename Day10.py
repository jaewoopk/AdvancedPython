n = int(input())

s = [0,0,0]
winner = 0
idx = 0
for i in range(n) :
    person1 = int(input())
    person2 = int(input())
    person3 = int(input())
    if (s[0] < person1) :
        s[0] = person1
    if (s[1] < person2) :
        s[1] = person2
    if (s[2] < person3) :
        s[2] = person3
    print(s)
for i in range(3) :
    if (winner < s[i]) :
        winner = s[i]
        idx = i

print("Person%d Win"%(idx + 1))