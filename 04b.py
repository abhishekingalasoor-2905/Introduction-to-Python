# operators 
# Assignment operators

a=10
b=20
a+=100 # short form of this a=a+100 
b*=100 # b=b*100
print(a)
print(b)

# Comparison operators
a=10
b=20
print(a==b) # equal to symbol
print(a>b)
print(a<b)
print(a !=b) # ! not equal to symbol

# Logical operators
print(True and True) # o/p = True (checking whether both are true)
print(True and False) # o/p = False
print(True or False) # o/p = True (checking whether atleast one is True)
print(False or False) # o/p = False
print(not(True)) # o/p = False
print(not(False)) # o/p = True
print(1>2) # o/p = False
print(1>2 or 1<2) # o/p = True
print(1>2 and 1<2) # o/p = False
print(1<2 and 3<4) # o/p = True
print(not(1>2)) # o/p = True (giving not word ,so it will change from False to True)

# Membership operators 
s = "Abhishek"
print("A"in s) # o/p = True (checking whether A is in Abhishek or not )
print("A"not in s) # o/p = Flase (because A is present in Abhishek )

s = "Abhishek"
s2 = "Abhishek.k"
print(("A" in s) and ("A"in s2)) # o/p = True mixing both logical and membership operators

# Bitwise operators
# check in notes 

print(False or True) # o/p=True