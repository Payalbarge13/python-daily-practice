#1 make a list in which a letter is present
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#2 not including apple into the list
newlist = [x for x in fruits if x != "apple"]
print(newlist) 

#3 loop comprehension

newlist = [x for x in range(20) if x < 15 and x % 2 == 0]
print(newlist)

#4 Return "orange" instead of "apple"
newlist =[x if x != "apple" else "orange" for x in fruits]
print(newlist)

#5 convert into uppercase
newlist = [x.upper() for x in fruits]
print(newlist)