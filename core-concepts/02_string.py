longtext='''
bharat
diwan
rollno.: c1-a4-61
'''
print(longtext)

name="bharat"
print(name[0]) #print index value

# String slicing
print(name[0:1])
print(name[0:4])
print(name[0:-1])

# fstring

name="Bharat"
country ="India"
income=10000
print(f"my name is {name} my country is {country} my income is {income*2}")
print(f"my name is {{name}} my country is {{country}} my income is {{income*2}}")

def str():
    '''
    this is a 
    doc string
    '''
print(str.__doc__) # This prints the docstring of a function, hence doc strings are not ignored

