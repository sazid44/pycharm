#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#Once a set is created, you cannot change its items, but you can add new items.
#the things that you can do with set : del ,join tuples,looping,checking items,remove or discard,pop,getting lenght
#If the item to remove does not exist, discard() will NOT raise an error.
#Both union() and update() will exclude any duplicate items.
set1 = {0,1,2,2,2}
set2 = set([4,5,6])
#UNION OF SETS(joining sets)
print(set1 | set2) # set3=set1.union(set2) or,set1.update(set2)
#INTERSECTION OF SETS
print(set1 & set2)  #set1.intersection(set2)
print(set1 - set2)