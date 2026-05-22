for i in range(1,20): # This prints values from 1 to 19
    print(i)

for i in range(1,20,2): # This prints values from 1 to 19 but with the seperation of 2
    print(i)
    
print("next")
# Break move out of the loop and ends there (doesnot print 3 and after)
for i in range(0,5):
    if(i==3):
        break;
    print(i)

# continue skips out of the current iteration (doesnot print only 3)
for i in range(0,5):
    if(i==3):
        continue;
    print(i)
    
for i in range(5):
    print(i)
    if i==3:
        break
else: # runs only when loop ends naturally or else it does not execute
    print("loop ended naturally")
