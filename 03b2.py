# string manupilation

first_name="Abhishek"
last_name="Ingalasoor"
full_name= first_name + " " + last_name #string concatenation
print(full_name)

message ="warning! "
print(message*8) # string repition
# or
message = "warning! "*8
print(message )
# string methods
print("bahubali".upper()) # upper = wrinting sentence in upper case
# or 
print(message.upper())

print("============")
print("BAHUBALI".lower())
#or
print(message.lower()) # lower = writing sentence in lower case

print("=============")
print("Bahubali ".strip()*2)
#or 
print(message.strip()) # strip = filling the left space

print("=============")
print(message .replace("warning" , "error")) # repalcing the words or statement
# there are more you can search in google string methods in w3 schools
# assigning the strings
name = 'Abhishek said "hello"'
print(name)
print("=======")

note = '''Abhishek said "hello"
        Teju said "hi"
        '''
print(note)

print("===========")
print(len(message)) # length

print("========================")


# Acessing string characters
# indexing starts from zero "0"
# ex = Abhishek = A=0,b=1,h=2,i=3,s=4,h=5,e=6,k=7  , A=1,b=2,h=3.i=4,s=5,h=6,e=7,k=8
# ex 1) find b = index-1 , position-2
# index=position-1

name = "Abhishek"
print(name[2]) # indexing
#sub strings and string slicing
print(name[2:8]) # in last of any word or sentence we choose position not index so [2:8] not [2:7]
# o/p = hishek
print(name[2:7])# in last we see where should it stop so it is hishe (it actually stops in k but it will not include it)it will use position at last
# o/p = hishe
print(name[:8]) # o/p = Abhishek ,because it assumes that it starts from 0 and end at its last position
print(name[2:]) #o/p = hishek ,becuse it assumes to print from 2 index (start) and prints upto last 8th position
# Reverse indexing = In reverse indexing it starts from -1 not 0
# ex = Abhishek index = A=0,b=1,h=2,i=3,s=4,h=5,e=6,k=7
# reverse index = k=-1,e=-2,h=-3,s=-4,i=-5,h=-6,b=-7,A=-8
print(name[-4])
print(name[-7:-2])
print(name[-2:-7])

print("============")
print(name[:]) # o/p = Abhishek
 
# [start:end:step or skip]
print(name[::3]) # o/p = Aie , because it skips three words like Aie(three words gap in between)like it starts from A and skips 3 words (bh) and reach i and again goes to e by skiping(sh)

print("============")

# escape sequence (\)
s = "Abhi \n is good boy" # \n = jumping to next line (check output)
r = "Abhi \t is good boy" # \t = gives one tab distance between sentence (check output)
print(s)
print(r)
print(name[2:4]) 
print(name[:7])
print(name[-4:2:-1]) # it was going from kehsihebA(in this statment it is forward because we used -1) and it choose 4=s and stops at 2=h and again it goes from Abhishek(in this statement it is backward ,because we used -1)