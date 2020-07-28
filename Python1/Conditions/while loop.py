#Looping System(while)
#With the while loop we can execute a set of statements as long as a condition is true.
n=1   #initialization
while n<5:   #condition
    print(n) #prints:1,2,3,4
    n=n+1   #update(increment)
else:print("while is over1")

n=1
while n<5:
    n=n+1
    print(n) #prints:2,3,4,5
print("while is over2")

# break statement
#if the condition matches,the break statement will break the loop
x=1
while x<10:
  print(x)  #prints:1,2,3,4,5
  if x==5:
      break
  x=x+1

print("while is over3")

x=1
while x<10:
  x=x+1
  if x==5:
      break
  print(x)  #prints:2,3,4

print("while is over4")

x=1
while x<10:
  if x==5:
      break
  x=x+1
  print(x)  #prints:2,3,4,5

print("while is over5")

x=1
while x<10:
  x=x+1
  print(x)  #prints:2,3,4,5
  if x==5:
      break
print("while is over6")



#if the condition matches,the continue statement will return that value to condition(while i<10)
# continue statement
i=1
while i<10:
  i = i + 1
  if i==5:
      continue
  print(i)



