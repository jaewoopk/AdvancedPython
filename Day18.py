def mark_num(List, num) :
    for i in range(4) :
        for j in range(4) :
            if (List[i][j] == num) :
                List[i][j] = 'X'

def check_line(List) :
    count = 0
    for i in range(4) :
        tmp1 = 0
        tmp2 = 0
        for j in range(4) :
            if (List[i][j] == 'X') :
                tmp1 += 1
            if (List[j][i] == 'X') :
                tmp2 += 1
        if (tmp1 == 4) :
            count += 1
        if (tmp2 == 4) :
            count += 1
        
    if (List[0][0] == 'X' and List[1][1] == 'X' and List[2][2] == 'X' and List[3][3] == 'X') :
        count += 1
    if (List[0][3] == 'X' and List[1][2] == 'X' and List[2][1] == 'X' and List[3][0] == 'X') :
        count += 1

    return count


mList = []
bList = []

for i in range(4) :
    list = []
    a, b, c, d = input().split()
    list.append((int)(a))
    list.append((int)(b))
    list.append((int)(c))
    list.append((int)(d))
    mList.append(list)

for i in range(4) :
    list = []
    a, b, c, d = input().split()
    list.append((int)(a))
    list.append((int)(b))
    list.append((int)(c))
    list.append((int)(d))
    bList.append(list)


while (True) :
    num = int(input())
    mark_num(mList, num)
    mark_num(bList, num)
    mBingo = check_line(mList)
    bBingo = check_line(bList)
    if (mBingo >= 3 and bBingo >= 3) :
        print(mList)
        print(bList)
        print("Draw!")
        break
    elif (mBingo >= 3) :
        print(mList)
        print("Minhyuk Win!")
        break
    elif (bBingo >= 3) :
        print(bList)
        print("Beomyeol Win!")
        break