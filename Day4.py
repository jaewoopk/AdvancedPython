n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())


for i in range(n2, n3 + 1) :
    for j in range(n4, n5 + 1) :
        if (i % 2 == 0 and j > 30) :
            break
        print("%02d%02d%02d"%(n1,i,j),end='')
        if (i == j) :
            print(" Lucky Day!")
        else :
            print()