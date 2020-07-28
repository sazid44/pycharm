'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
'''

for n in range(2, 11, 2):  #range(starting value, end before value, increment by value)
     print(n)
for x in range(2, 30, 3):
         print(x)

# printing the sum of user's given numbers
num = input("enter some numbers: ")  # getting user input
makeList = num.split()
sum = 0
for x in makeList:
            sum = sum + int(x)
            print(sum)
#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#no error
for x in [0, 1, 2]:
  pass

#looping through a string
for x in "banana":
  print(x)