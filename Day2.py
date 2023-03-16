# dice1 = int(input())
# dice2 = int(input())

# if (dice1 % 2 == 0 and dice2 % 2 == 0) :
#     print("All dices are even!")
# elif (dice1 % 2 == 1 and dice2 % 2 == 1) :
#     print("All dices are odd!")

dice1 = int(input())
dice2 = int(input())

sum = dice1 + dice2

if (sum % 3 == 0 and sum % 6 == 0) :
    print("%d is multiple of 3 and 6"%sum)
elif (sum % 3 == 0) :
    print("%d is multiple of 3"%sum)
else :
    print("%d is not multiple of 3 or 6"%sum)