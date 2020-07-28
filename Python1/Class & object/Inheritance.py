#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class phone:
    def call(self):
        print("call")
    def message(self):
        print("message")
class samsung(phone): #Inheritance
    def photo(self):
        print("photo")

s=samsung()
s.photo()
s.call()
print(issubclass(samsung,phone))

# override and recall mehtod
class phone_:
    def __init__(self):
        print("phone class")
class samsung(phone_):
     def __init__(self): #overrides
#By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.
        super().__init__() #recalls
        print("samsung class")
samsung()


#Types of Inhertance
#multi-level inheritance
class A:
    def display1(self):
      print("This is A")

class B(A):    #B now inherits A
    def display2(self):
      print("This is B")

class C(B):    #C now inherits both A and B
   def display3(self):
     print("This is C")

C().display3()
C().display2()
C().display1()

 #multiple inheritance
class X:
    def display(self):
        print("This is X")
class Y():
    def display(self):
        print("This is Y")
class Z(X,Y):  # Here principle is X
    pass   #if there is a function in Z then that will be the principle

Z().display()
