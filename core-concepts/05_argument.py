def average(a=9,b=1):
    print("average",(a+b)/2)
average() # Default argument
average(10,20)

def multiAverage(*numbers): #  * Takes numbers as tuple
    sum=0
    for i in numbers:
        sum+=i
    print("average: ",sum/len(numbers))
multiAverage(1,2,3,4,5,6)

def dictname(**name): # ** Takes name as dictionary
    print("first name:",name["fname"],"\nmiddle name:",name["mname"],"\nsurname:",name["sname"])

dictname(fname="bharat",mname="dhar",sname="diwan")

    