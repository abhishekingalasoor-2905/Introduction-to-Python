# datatypes and variables,arithmetic operations
name = "Abhishek" # string data type


age=19 # int data type


weight=56.5 # float data type

is_student= True # boolean data type
is_teacher= False
print(type(name)) # we can know the datatype by using type word
print(type(age))
print(type(weight))
print(type(is_student))
x=None
print(type(x))

s="100"
s_int=int(s) # conversion of datatype; for example:form string to integer
print(type(s))
print(type(s_int))
a=10
b=3
print(f"before swapping a={a} b={b}") # swapping string from formated method
# formated string assign the value of variables directly into the string or print statement
# formated string : allow you to embed variales and expression directly into the string literals 
print("before swapping",a,b) # we didn't use the foramted string so we have assigned the variables value in this
a,b=b,a # swapping takes palce here 
print(f"after swapping a={a} b={b}") # formated string
print("after swapping", a , b) # not a formated string
# Arithmetic operations
print(a+b) # addition
print(a-b) # substraction 
print(a*b) # multiplication
print(a/b) # division 
print(a//b) # floor division takes the round off of floating point; for example : 0.3 is consider as 0
print(a%b) # modulus operator for example gives the remainder , 10%3 = 1 :remainder ,3%10 = 3:remainder
print(a**b) # exponentiation operator for example giving power ,2**3 = 2^3(cube)
print(2**2)
print(a+b-a-b*a)

a,b=10,20 # another method of swapping 
temp=a
a=b
b=temp
print(f"after swapping {a} {b}")
