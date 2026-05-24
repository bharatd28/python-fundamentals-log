f=open("myfile.txt","r") # assigns variable to opens the file in read mode
# f=open("myfile.txt","rb") # reads file in binary format 
# f=open("myfile.txt") if no mode is assigned it takes read mode as default
text=f.read() # assign variable to read the file
print(text) # prints variable
f.close() # closes the file

f=open("myfile.txt","w") # write mode
f.write("bharat dhar diwan") # it rewrites the entire file
f.close()

f=open("myfile.txt","a") # appends
f.write(". roll no.: 61")
f.close()

with open("myfile.txt","r") as f:
    
    print(f.read())
