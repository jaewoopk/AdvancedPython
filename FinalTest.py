user_info = {'name' : 'David', 'age' : 21, 'address' : 'Gwangjin-gu, Seoul'}

n = int(input())

for i in range(1,n + 1) :
    str = input("Edit #%d\n"%i)
    answer = input()
    user_info[str] = answer

print("\nUSER INFO")

for i in user_info :
    print("%s : %s"%(i,user_info[i]))



#     3

# Edit #1
# name
# Amin
# Edit #2
# hobby
# swim
# Edit #3
# age
# 29

# USER INFO
# name : Amin
# age : 29
# address : Gwangjin-gu, Seoul
# hobby : swim