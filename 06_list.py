marks=[1,2,3,4] # list

'''
lists are ordered
lists are mutable
any kinds of data types can be inputed in a list
slicing also works on lists
0 indexing
'''
# List compreshenssion

lst=[i for i in range(0,5)]
print(lst)
lst=[i for i in range(0,5) if i%2==0]
print(lst)

# List methods
lst=[12,1,24,2,3,4,16,5,6]


lst.append(7) # adds an element in the list

lst.sort()
lst.sort(reverse=True) # Sorts the list in reverse order

lst.reverse() # Reverses the current list

print(lst.index(12)) # returns the index of an elemennt

print(lst.count(1)) # counts the occurence of an elemnet in the list

m=lst
m.append(10) # m is not a different list m is a reference to lst hence changes in m changes lst itself
print(m)

m=lst.copy() # This infact copies the list as we intended
m.append(69)
print(m)

lst.insert(2,69) # Inserts element 69 in index 2

k=[11,22,33]
lst.extend(k) # This extends lst by adding list k to its end

p=[699,16,12]
o=p+lst # This merges the two lists by adding the second list to the first (concatinate)
print(o)

lst.pop() # removes the last element
lst.pop(2) # pops element at given index

print(lst)