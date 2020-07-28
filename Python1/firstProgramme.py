'''
Indentation refers to the spaces at the beginning of a code line.
Python uses indentation to indicate a block of code.
You have to use the same number of spaces in the same block of code.

Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''
##Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(y)
# you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(y)

name = "sazid"
age = 17
gpa = 3.97
# Concatenation
print("My age is ", age, "and gpa is ", gpa)  #
print("This is end", end=" .")  # use of end
print("My name is " + name)

# Use of some escape characters
print("This is a Backslash\"")  # printing the backslash
print('It\'s great')  # printing the apostrophy
print("hello\nworld")  # new line
print("hello \r world")
print("hello \t world")  # tab
print("hello \f world")  # form feed
print("hello\b world")  # backspace

# formating
num1 = 20
num2 = 30
print(f"{num1}+{num2}={num1 + num2}")  # prints: 20+30=50
'''
Global Variables
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.
Example:
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
If you create a variable with the same name inside a function, this variable will be local, 
and can only be used inside the function. The global variable with the same name will remain as it was, 
global and with the original value.
Example:
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)

The global Keyword:
If you use the global keyword, the variable belongs to the global scope:
use the global keyword if you want to change a global variable inside a function.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
'''
# example of some type casting
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'
x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0
w = float("4.2")  # w will be 4.2

# python_strings
# You can assign a multiline string to a variable by using three quotes(single 0r double):
# the line breaks are inserted at the same position as in the code.
a = """My name is sazid.
I am 17 years old.   
very good."""
print(a)
# strings in Python are arrays of bytes representing unicode characters.
# Python does not have a character data type, a single character is simply a string with a length of 1
a = "Hello, World!"
print(len(a))
print(a.strip())  # returns "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))  # returns ['Hello', ' World!']
# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
x = "el" in a
print(x)
x = "ain" not in a
print(x)

# swaping method
a = 10
b = 20
a, b = b, a
print(a)
