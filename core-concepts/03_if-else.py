# Boolean output
a=18
print(a>18)
print(a<18)
print(a==18)
print(a>=18)

# Match
a=20
match a:
    case 18:
        print("hi")
    case _ if a!=18: #_ is default state 
        print("no")
    case _ if a>18: # once a case is matched it stops there
        print("no greater")

b=int(input("enter integer"))
print("value greater than 10") if b>10 else print("value less than 10") if b<10 else print("value=10")


