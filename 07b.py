# Dictonaries{} operations ,methods and functions
# contains key value pairs
# dictonaries={key:value} key value pairs

birthday={
    "Abhi":"8-7-2008",
     "Teju":"29-3-2006"
}
print(birthday)
print(type(birthday))
b={1,2,3}
print(type(b)) 
# this is the difference between sets and dictonaries 
# dictonaries contains key value pairs sets doesn't contains key value pairs
# dictonaries are unordered and mutable (changeble)
# Accessing dictonaries elements :-

print(birthday["Abhi"]) # accessing value through keys in square brackets[]
# using get method to access values,which is safer because it doesn't show keyerror
print(birthday.get("sudeep")) # shows none because i didn't enter value for this key
# or
print(birthday.get("sudeep","not found"))

# Adding and updating dictionary elements :-
# Adding sudeep to the list(during runtime)
birthday["sudeep"]="02-09-1973"
print(birthday)
# updating Abhi date of birth from 2008-2007
birthday["Abhi"]="8-7-2007"
print(birthday)

# removing elements from dictionaries:-(pop,del,clear)
birthday.pop("Teju") # we can also assign variables like x
print(birthday)

del birthday["sudeep"]# using square braces,we cannot assign variables
print(birthday)

# clear
birthday.clear()
print(birthday)

dob={
    "Dhoni":"7-7-1981",
    "prabhas":"23-10-1979",
    "sushant":"21-1-1986"

}
print(dob)

# dictionary methods:-(keys(),values(),items(),update())

print(dob.keys())# only keys no values
print(dob.values())# only values no keys
print(dob.items())# print both keys and values gives in tuples formats[]
new_dob={"Abhishek":"08-07-2007"}# updating new key value pair
dob.update(new_dob)
print(dob)

# also we can use any datatypes
g={
    "hi":123,
    "hello":456
}
print(g)
# well structured

item1={
    "name":"milk",
    "weight":2,
    "price":68
}

item2={
    "name":"sugar",
    "weight":3,
    "price":90

}

items=[item1 , item2 ]
print(items)
print(f"total weight: {item1["weight"]+item2["weight"]}kg")
 
