time = int(input())
minute = int(input())

M = int(input())
N = int(input())

h = M // 60
m = M % 60
for i in range(N) :
    if (time >= 22) :
        print("Emergency!")
        break
    print("%02d:%02d Carrot Time!"%(time,minute))
    time += h
    minute += m
    if (minute >= 60) :
        minute %= 60
        time += 1



