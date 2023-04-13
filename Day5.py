# a = int(input())
# b = int(input())
# c = int(input())

# avg = (a+b+c)/3
# print("Average = %.2f"%(avg))

# if (avg < 60) :
#     print("FAIL")
# else :
#     if (a < 40 or b < 40 or c < 40) :
#         print("FAIL")
#     else :
#         print("PASS")


# a = int(input())
# b = int(input())
# c = int(input())

# mx = max(a,b,c)
# mn1 = min(a,b)
# mn2 = min(b,c)

# if (mn1 + mn2 > mx) :
#     print("YES")
# else :
#     print("NO")

person = int(input())
color1 = input()
color2 = input()

print("color 1 values(RGB): %s"%color1)
print("color 2 values(RGB): %s"%color2)

if (color1 == color2) :
    print("Just same colors")
elif (person == 1 and (color1 == "100" and color2 == "010")) :
    print("Red and Green")
elif (person == 1 and (color1 == "010" and color2 == "100")) :
    print("Green and Red")
elif (person == 2 and (color1 == "110" and color2 == "001")) :
    print("Yellow and Blue")
elif (person == 2 and (color1 == "001" and color2 == "110")) :
    print("Blue and Yellow")
