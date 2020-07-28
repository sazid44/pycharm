import re
pattern=r"colour"
if re.search(pattern,"Red is a colour"):
    print("Matched")
else:
   print("Not matched")
#match method finds the pattern first in the string
#search method finds the pattern all over the string
#find all method finds pattern and prints a list including all the matched pattern

pattern1=r"colour"
text="Red is a colour"
match=re.search(pattern1,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

#search and replace
pattern2=r"colour"
text1="Red is a colour.It is a nice colour."
print(re.sub(pattern2,"color",text1,count=1))
#character class
import re
pattern=r"[a-z][A-Z][0-9][aeiou]" #you have to maintain sequence
if re.match(pattern,"aA0e is a colour"):
    print("Matched")
else:
   print("Not matched")



#Meta character
'''
1.*=from 0 to 1
2.+= 1 or more
3.(.)=any character
4.?=from 0 to 1
5.a{1,3}$=means from 1 to 3 a can be used
'''