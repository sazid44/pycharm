from Module.module import *
tri(4, 5)
rec(2,3)
#another way
from Module import module, module as x

module.tri(4, 5)
#renaming the module
x.tri(4,5)


#there is a built-in function to list all the function names (or variable names) in a module. The dir() function:


#List all the defined names belonging to the platform module:

import platform

x = dir(platform)
print(x)