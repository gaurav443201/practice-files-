try:
    a =  int(input("hey,Enter the number:"))
    print(a)

except ValueError as v:
    print("heyyyyy")
    print(v)
    
else:
    print("i am inside else")
