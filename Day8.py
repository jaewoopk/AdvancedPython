n = int(input())

s = []

for i in range(n) :
    s.append(int(input()))

a = int(input())
b = int(input())


print(s)
for i in range(a,b + 1) :
    for j in range(i,b + 1) :
        if (s[i] < s[j]) :
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            print(s)