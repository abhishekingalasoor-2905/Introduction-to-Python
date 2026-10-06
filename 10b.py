# For loops
# iterate over a sequence (list,tuple,string or range)
# range(1,10)=(1,2,3,4,5,6,7,8,9)
#also contains step like [start,stop,step]
'''
for i in range(1,11):
    print(i,end="  ")# with end using the order of sequence comes in horizontal manner
    print(i) # without end the sequence comes in vertical order
# only when we do them separatly
print("------------------")
# loops over lists
bag=["red","green","yellow"]
for ball in bag: # it means for each ball in bag
    print(ball)
print("-----------------")

# range 
for i in range(1,11,2):
    print(i,end=" ")
print("-----------------")

# looping over strings and enumerate

name="Abhishek"
for letter in enumerate(name):
    print(letter)
    print("---------------------")


name="Tejaswini"
for index,word in enumerate(name): # we should use index if we didn't use indexz it shows its not defined
    print(word*(index+1))
print("----------------------")

l=[12,123,345,678]
for index,num in enumerate(l): # we should use index if we didn't use indexz it shows its not defined
    print(f"{num} is in {index}th index")
print("--------------")

# using break in for loop
cities=["bengaluru","mumbai","chennai","hyderabad"]
for city in cities:
    if city=="chennai":
        print(f"found  {city}!")
        break # if we didn't use break it also print futher words also (if you have doubt once remove break statement and check)
    print(city)
print("----------------")

cities=["bengaluru","mumbai","chennai","hyderabad"]
for city in cities:
    if city=="chennai":
        print(f"found  {city}!")
        continue # it a statement used to continue further statement also 
    print(city)
print("-----------------")

# using else in loops
j=[7,18,45,10]
for num in j:
    print(num)
    if num==10:
        break
else: # we use else statement because it is used during break staement (once run and check)
    print("All printed")
print("-------------------")
'''
# loops using dictonaries
d={"name":"Abhishek", "age":22,"income":1}
for key,value in d.items(): # we are converting dictionaries to tuples because we want to print both key and value both
    print(key," ", value)


# Nested loops
for i in range(2,11):
    for j in range(1,11):
     print(f"{i}*{j}={i*j}")
