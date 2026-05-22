tup=(1,2,3,4) # Tuple
tup=(1) # this is not a tuple but is an integer
tup=(1,) #this is a tuple

'''
ordered
immutable
any number of data types can exist in a tuple
0 indexing
if you want to change a tuple convert it to list than do changes in the list and convert list to tuple
'''
# Slicing is same as Lists
# But Slicing return a new tuple .while in list the same list is modified

tup=(0,1,2,3,4,5)
print(tup[1:3])
print(tup[2:5])
 
# Methods
tup=(1,2,3,4,4,5,6,32,23,53,4)

# we can concatenate 2 tuples without converting them to list

print(tup.count(4))

print(tup.index(4))
print(tup.index(4,5,)) # This gives the index of value 4 between index's 5 and last element





