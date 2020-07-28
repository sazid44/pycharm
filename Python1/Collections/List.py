                              #  HISTORY OF LIST  #
#A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
a=[1, 2, 3 ,4 ,5 ,6]
print(a[0]) #prints the first item of list
print(a[-1]) ##prints the last item of list
print(a[1:4]) #prints from index 1 to 4(2,3,4)
#and note that the item in position 4 is NOT included
print(a[1:]) #By leaving out the end value, the range will go on to the end of the list
print(a[:4]) #By leaving out the start value, the range will start at the first item ==(1,2,3,4,)
a[0]=0 #changing the first value
a.append(7) #To add an item to the end of the list, use the append() method
a.insert(1,8) #To add an item at the specified index, use the insert() method==a.insert(index number,value of that index)
a.sort() #sorts the list
a.reverse()  #Reverses the order of the list
a.remove(3) #The remove() method removes the specified item
a.pop() #The pop() method removes the specified index, (or the last item if index is not specified):
del a[2] #The del keyword removes the specified index,The del keyword can also delete the list completely
#a.clear() #The clear() method empties the list
b=a.copy() #Make a copy of a list with the copy() method
b=list(a) #Another way to make a copy is to use the built-in method list().
c=['a','b','c']
d=a+c #joining two lists
a.extend(c) #you can use the extend() method, which purpose is to add elements from one list to another list
#here the items of c list is added to a list
print(len(a))
t=tuple(a) #we can convert a list to tuple
for x in a:  #Print all items in the list, one by one:
    print(x)
if "a" in c: #To determine if a specified item is present in a list use the in keyword:
  print("Yes, a is in the  list")






