
#if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.

mark=40
num=30
# 1 statement
if num<mark:print("pass")

# 2 statements
if num > mark:
  print("pass")
else:print("fail")

# 3 statements
if num > mark:
  print("pass")
elif num==mark :
  print("not pass")
else:print("fail twice")

# only if
if num>0:
    print(0)
if mark>-1:
    print(-1)
if mark >num:
    print(num)

#inner if(also logical operator {and,or})
if num>0 and mark>0:
   print("correct")
   if mark>10 or num<mark:
    print("invalid")
   else:print("inner else")
else:print("outer else")

#Ternary operator
x=10
y=20
print(x if x>y else y)

#counting the letters,digits and words of given input
numofwords=0
numofdigits=0
numofletters=0
p=input("Enter your comment:")
for s in p:
  s=s.lower()
  if s>='a' and s<='z':
   numofletters=numofletters+1
  elif s>='0' and s<='9' :
   numofdigits=numofdigits+1
  elif s==' ':
   numofwords=numofwords+1
print(numofletters)
print(numofdigits)
print(numofwords+1)

