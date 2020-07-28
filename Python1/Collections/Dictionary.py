#A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
# Dictionary mehtod
dict={
    'a': 'muzahidul',
    'b': 'you can access the dictionary by using defined key',
    'c': 'sazid'
}
print(dict["a"]) #print(Dic.get('a'))
print(dict.get('d', 'you are a fool'))
dict['c']="islam" #changing the value
dict['d']="sazid" #changing the value
print(dict)
dict.pop(b) #The pop() method removes the item with the specified key name
dict.popitem() #The popitem() method removes the last inserted item
dic=dict(dict) #making copy

#Print all key names in the dictionary, one by one:
for x in dict:
  print(x)

#Print all values in the dictionary, one by one:
for x in dict: #or,for x in thisdict.values()
  print(dict[x]) #print(x)

#Loop through both keys and values, by using the items() method:
for x, y in dict.items():
  print(x, y)


#Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#if you want to nest three dictionaries that already exists as dictionaries:
#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

