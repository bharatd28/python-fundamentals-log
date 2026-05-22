
try:
    a=int(input("\nenter an integer"))
    print(2*a)
except Exception as e:
    print(e)
finally: # runs regardless
    print("wow")

def func():
    try:
        return 1
    finally: # outputs even if there is a return code above
        print("run")
print(func())

# custom errors
a=int(input("enter value between 1-10:"))
if (a<1 or a>10):
    raise ValueError("Value should be btw 1-10")




