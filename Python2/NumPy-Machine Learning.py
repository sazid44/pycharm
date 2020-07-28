import numpy as numpy
from scipy import stats
arr=numpy.array([1,2,3,4,5])
print(arr)
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)

print(x)


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)