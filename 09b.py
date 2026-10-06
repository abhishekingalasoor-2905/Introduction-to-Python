# Loops and break,continue
# while loop
# repeats the sentence until it reaches or true its specific condition

condition=True
while condition:
    print("condition is True")
    break
print("----------------------")

is_failed=True
i=1 #i means attempt
while is_failed and i<=100 :
    print(f"Try{i}")
    i=i+1
print("I gave up !!!!!!!!!!")

print("---------------------")
is_failed=True
i=1
while is_failed:

    print(f"try {i}")
    i=i+1
    if i>100:
        break
print("I gave up")
print("-----------------------")

is_failed=True
i=1
while is_failed:
    
    if i %2!=0: # is not even (% reminder)
        i=i+1
        continue
    print(f"attempts {i}")
    i=i+1
    if i>100:
            break
print("I gave up!!!!!!!!!!")

 
# attempt 1,2_ _ _ _ iteration
# nested loop
i=0
while i<=100:
    x=0
    while x<i:
        print("Pramod",end="-")
        x+=1
    print("")
    i+=1
print("--------------------------------")

pin="1234"
trials =1
while trials<3:
    input_pin=input(f"Trial-{trials} | PIN ==")
    trials+=1

    if input_pin==pin:
        print("correct")
        break
    else:
        print("incorrect")  
    



    
    
  


