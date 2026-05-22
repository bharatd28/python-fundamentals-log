def welcome():
    print("welcome")

# welcome() # this runs function when imported

if __name__=="__main__": # runs only if the function is being executed on this file and not on being imported 
    print(__name__) # this shows which file is calling the function
    welcome()

