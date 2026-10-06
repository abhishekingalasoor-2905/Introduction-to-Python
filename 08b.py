# Conditional statements
# if=checks whether true ,if its true then it blocks that condition and prints


# else ,elif
#if:-
x=10
if x==10:
    print("yes x is 10") # indentation(one tab gap)
print("-----------------------------------")


#if and else:-
x=27
if x%2==0:
    print("yes x is even")
else:
    print(" x is odd")
print("----------------------------------")


# if,else,elif
signal= input("what is the color of signal :")
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready")
else:
    print("go")
print("-------------------")

# logical operators (and,or,not)

att = 75
is_teacher_friend=True
if att>=75:
    print("exam")
elif att<75 and is_teacher_friend==True: # and operator
    print("exam")
else:
    print("no exam")


print("-----------------")

att=85
is_teacher_freind=True
if att>85 or is_teacher_freind:
    print("exam")
else:
    print("no exam")

# nested if else statement

gender=input("gender :")
age=int(input("age :")) # using int data type
if gender=="female":
    print("free ticket")
else:
    if age < 5:
        print("ticket free")
    elif age <=12:
        print("you are child get discount")
    elif age>=65:
        print("senior citizen ticket")
    else:
        print("you get full fare. ")



    




