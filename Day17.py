def transScore(k) :
    if (k == 'A') :
        return 4
    elif (k == 'B') :
        return 3
    elif (k == 'C') :
        return 2
    elif (k == 'D') :
        return 1
        
n = int(input())

nameList = []
hakbunList = []
scoreList = []

for i in range(n) :
    nameList.append(input())
    hakbunList.append(input())
    a, b, c = input().split()
    a = transScore(a)
    b = transScore(b)
    c = transScore(c)
    x, y, z = input().split()
    x = (int)(x)
    y = (int)(y)
    z = (int)(z)
    score = (a * x + b * y + c * z) / (x + y + z) 
    scoreList.append(score)

name1, name2 = input().split()
index1 = 0
index2 = 0

for i in range(n) :
    print("%s : %.2f"%(nameList[i],scoreList[i]))
    if (name1 == nameList[i]) :
        index1 = i
    elif (name2 == nameList[i]) :
        index2 = i

if (scoreList[index1] > scoreList[index2]) :
    print(hakbunList[index1])
elif (scoreList[index1] < scoreList[index2]) :
    print(hakbunList[index2])
else :
    if ((int)(hakbunList[index1]) > (int)(hakbunList[index2])) :
        print(hakbunList[index2])
    else :
        print(hakbunList[index1])