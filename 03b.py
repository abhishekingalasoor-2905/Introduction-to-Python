# input and output /prints and comments
boy_name=input("boy name: ")
boy_age=int(input("boy age: "))
girl_name=input("girl name: ")
girl_age=int(input("girl age: "))
age_diff=abs(boy_age-girl_age) # abs means absolute value, like modulus(like positive values only) and we also made substraction of int and int itself so the age_diff also is an int
print(age_diff)
print(f'{boy_name} loves {girl_name}.age difference is {age_diff}')
print(boy_name + " loves " + girl_name + ". age difference is " + str(age_diff) ) # we have made concatenation like adding so we used string to the age_diff, so we can say that we can concatenate only of same data type 
# triple code for writing long code
