try:
    a =  int(input("hey,Enter the number:"))
    print(a)

except ValueError as v:
    print("heyyyyy")
    print(v)
    
finally:
    print("i am inside finally")


