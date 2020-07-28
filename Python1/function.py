#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma.

def sazid(a,b):
    sum=a+b
    print(sum)
sazid(1,2) #calling a function

#method of returning value
def add(a,b):
    sum=a+b
    return sum
add(1,2)
print(add(1,2))

# use of lambda function
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
a=(lambda p,q:p+q)(2,3)
print(a)

#use of map function
def square(a):
    return a*a
array=[1,2,3]
result=list(map(square,array))
print(result)

#list comprehension:(easing map)
arrayList=[1,2,3]
result1=[x*x*x for x in arrayList]
print(result1)

#use of filter function
array1=[1,2,3,4,5]
result2=list(filter(lambda x:x-1==1,array1))
print(result2)

#list comprehension:(easing filter)
arrayList1=[1,2,3]
result3=[x for x in arrayList1 if x/2==1]
print(result3)

#ZIP function
name=['a','b']
roll=[1,2]
print(list(zip(name,roll,'ab')))

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:
def xargs(*n):
  sum = 0
  for x in n:
    sum=sum+x
  print(sum)
xargs(1,2,3)

#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function,
#add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def xxargs(**i):
    print(i["id"])
xxargs(id=1,name='sazid')

#If we call the function without argument, it uses the default value:


def my_function(country = "Norway"):
  print("I am from " + country)

my_function()


#Passing a List as an Argument
#You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

# Recursion is a process where a function can call itself
def fact(o):
    if o==1:
        return 1
    else:
        return o * fact(o-1)
print(fact(5))


#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))