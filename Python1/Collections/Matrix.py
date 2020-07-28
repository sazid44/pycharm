#Introduction to matrix
matrix=[
    [1,2,3],
    [4,5,6],
]
#matrix[0][1]=10 ...changing the value
#print(matrix[0][1])
for row in matrix:
    for col in row:
        print(col)

#stack
stack=[]
stack.append('c++')
stack.append('java')
stack.append('php')
print(stack)
stack.pop()     #kicks out the last appended or pushed input
print(stack)

#queue
from collections import deque
queue=deque(['a','b','c'])
queue.popleft()   #kicks out the first one(from left side)
queue.popleft()
queue.popleft()
print(queue)
if  not queue:
    print("ok")

