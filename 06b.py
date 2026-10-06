 # Tuple() and Sets :-

# A tuple is a collection of items that is orderd and immutable(unchanged)
# Tuples are similar to lists,but once a tuple is created 
# You cannot modify it
# They are often used to group related data together

genders=("male","female","other")
print(genders)
print(type(genders))
print(genders[0])
print(len(genders))

boy=("Abhi",) # should add comma(,) ,because its tuple if we don't add comma(,) it will be string
print(boy)
print(type(boy))
# cannot add the tuples elements inside the tuple .Only we can add a whole one tuple to another tuple
# tuple to tuple addition
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
# or
combined_tuple=tuple1+tuple2
print(combined_tuple)

# tuple repition
y=(1,2)*3
print(y)

# memeberships in tuples
t=(1,2,3,4,5,6)
print(2 in t) # true

# methods in tuples
r=(1,2,3,4,5,1,2,1,3,1)
print(r.count(1)) # 4
print(r.index(1)) # 0
# tuples are faster than list
# can be used as  key in dictionaries

# nested tuples 
i=("k","j","l",(1,2,3))
print(i)

# SETS{}:-
# A sets is a collection of unique items that is unordered and unindexed
# Sets do not allow duplicate values
# Sets are useful for performing operations like union,intersection,and difference
s={120,6,5} # {120,5,6} unordered
print(type(s))
print(s) 
# cannot indexed or no indexing
s2=set((1,23,4))# should use only one arguments at once so use two times of brackets
print(s2)
print(type(s2))
#{} don't use this as empty because it shows dictionary,so use set()

# Operations (unions(|) and intersection(&) and difference(-))
s1={1,2,3,4}
s2={3,4,5,6}
print(s1 | s2) # unions(|)
print(s1 & s2) # intersections(&)
print(s1-s2) # difference(-) removes the repeated elements of s1 so,1,2

# sets methods
p={1,2,3,4,5}
print(type(p))
print(p.pop()) # removes random element
p.add(6)
print(p)
p.remove(4)
print(p)
p.clear()
print(p)






