#list[] in python

item1="bru"
item2="milk"
item3="sugar"
print(item1,item2,item3)
# else we can write it in one list so,we use list in python
items=["bru","milk","sugar"] # its called list
# A list is an orderd(index) collection,mutable 
# And allows duplicate elements
#list can hold items of different data types,such as integer,strings,or even other lists
print(items)
# And also we can do index printing also
print(items[0]) # bru
print(items[1]) # milk
print(items[2]) # sugar
l=[1,"bru",True,[1,2,3]] # we can use any data type at once
print(l)
# lists are mutable:-(changeable)

items.pop() # remove last elements of the list (items)
print(items)
items.pop(0) # remove first elements
print(items) 

items.append("biscuit") # it adds in the list (items)
print(items)

items.remove("milk") # removes which elements we want in list (items)
print(items)

items.insert(0, "spoon") # insert which ever poistion we want
print(items)

items.clear() # removes complete list (items)
print(items)

items=["sugar","milk","sugar"]
items[0]="tea powder" # repalce (bru to tea powder) elements which ever position we wants
print(items)

# slicing the list:- trys to extract the portion of list
#[start:stop:step]
z=["a","b","c","d"]
print(z[0:3]) # a b c(3-1)
print(z[0::3]) # a d (no (3-1))
z2=z[0:3] # we can replace z with z2
print(z2) # a b c

# common functions:-
# length
k=[1,2,3,4,5,6,7,8,9]
print(k)

print(len(k)) # tells the length of the list

# sorted 
x=[1,9,3,7,6,5,8]
print(sorted(x)) # tell to list to be in descnding order to ascending order
# or
sorted_x=sorted(x)
print(sorted_x)

# sum 
y=[10,20,30,50,80] # adds every number in the list
print(sum(y))
# or 
sum_y=sum(y)
print(sum_y)
'''
t=["abhi",1,"aman",2]
print(sum(t)) # shows error becaus eof different data types
'''
# index
d=[1,3,4,6,7]
print(d)
print(d.index(3)) # 3 is in 1st index

# count

n=[6,5,8,6,6,7,8,6]
print(n.count(6)) # how many times we added the 6 number 4 times 

# reverse 
u=[1,2,3,104,5,6,7,20,9]
sorted_u=sorted(u)
print(sorted_u)
rev=sorted_u.reverse() # reverse the sorted list(u)
print(sorted_u)

# Nested list

m=[[1,2,3],[5,6,7],[8,9,10]]
print(m) # nested in one list
# index in nested list
print(m[0]) # 1 2 3
print(m[0][1]) # element 2 will print 

# data type in list
v=[1,2,3,4,5,6]
print(type(v))

# membership operations
o=[1,2,3,4,5]
print(3 in o)


