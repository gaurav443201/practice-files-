f = open("file.txt")
print(f.read())
f.close()

#the same statement can be written with using with statement like this

with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file
   
