#NameError,ZeroDivisionError,TypeError,IndentationError,IndexError

try:
    def a(x,y):
     division=x/y
     print(division)
    a(2,2)
except (NameError,ZeroDivisionError,TypeError,IndentationError,
        IndexError,ValueError,EnvironmentError,SyntaxError):
     print("ok")
finally:
    print("not ok")

# error handling with raise
def voter(age):
    if age<18:
        raise ValueError("ok")
    return "not ok"
try:
    print(voter(20))
except ValueError as e:
    print(e)
