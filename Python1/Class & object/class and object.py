'''
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties,
or other operations that are necessary to do when the object is being created:

Objects can also contain methods. Methods in objects are functions that belong to the object.

The self Parameter:
The self parameter is a reference to the current instance of the class,
 and is used to access variables that belong to the class.
The self parameter is a reference to the current instance of the class,
and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like,
but it has to be the first parameter of any function in the class:

class student:
    def set_value(self,roll,gpa):
        self.roll=roll
        self.gpa=gpa
    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")

rahim = student()# Now,rahim is a object of class student
rahim.set_value(1,2)
rahim.display()
'''
class student:
    # use of Constructor
    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll:{self.roll},GPA:{self.gpa}")

rahim = student(1, 4) # Now,rahim is a object of class student
rahim.roll=3 #changing the value
#we can delete parameter or object (del rahim.roll or del rahim)
rahim.display()
karim = student(2, 3)
karim.display()



from abc import ABC,abstractmethod
class shape:  #for declaring a abstract method,the shape class is now a abstract class,it can't have object now.
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2= dim2
    @abstractmethod  
    def area(self):
        pass

class rectangle(shape):
 def area(self):
    area = self.dim1 * self.dim2
    print("Area is:", area)

class triangle(shape):
 def area(self):
    area=0.5*self.dim1 * self.dim2
    print("Area is:",area)

r=rectangle(2,3)
r.area()

t=triangle(2,3)
t.area()


##Use of magic methods(__str__ , __eq__ .....)
class bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def __eq__(self, other):
        return self.name==other.name and self.color==other.color #prints true

    def __str__(self):
        return(f"Name={self.name},Color={self.color}") #prints false

    def display(self):
        print(f"Name={self.name},Color={self.color}")

bike1=bike("moto","red")
bike2=bike("moto","red")
print(str(bike1))

print(bike1==bike2)