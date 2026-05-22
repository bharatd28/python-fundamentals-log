s={1,2,3,4,5,2} # set
s={} # but this is not an empty set its an empty dictionary
s=set() # this is an empty set
'''
unordered
values cannot be repeated
sets are mutable but the values cannot be changed they can be deleted/added but not replaced directly
'''
s1={1,2,3,4}
s2={4,6,7,2}

print(s1.union(s2)) # union

print(s1.intersection(s2)) # intesection

s1.update(s2) # this adds values of s2 in s1
print(s1,s2)

s1={1,2,3,4}
s2={4,6,7,2}

print(s1.symmetric_difference(s2)) # prints vaues which are not common in both

print(s1.difference(s2)) # prints values which are in s1 but not in s2

print(s1.isdisjoint(s2)) # gives boolean value if the sets are disjoint i.e. there are no intersection between the two sets

print(s1.issubset(s2))

print(s1.issuperset(s2))

s1.add(12)
print(s1)

s1.remove(12)
print(s1)

s1.discard(12) # if we try to discard an element which is already not present this will not raise an error while remove function will raise.
print(s1)

item=s1.pop() # removes and returns any randome value
print(s1)
print(item)

s2.clear() # cleares all elements of a set

del s2 # deletes a set
print(s2)