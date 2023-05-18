dic = {}

while(True) :
    n = int(input())
    if (n == 0) :
        break
    elif (n == 1) :
        name = input()
        score = int(input())
        dic[name] = score
    elif (n == 2) :
        name = input()
        if (name not in dic) :
            print("No student")
        else :
            print("Name = %s, Score = %d"%(name,dic[name]))
    