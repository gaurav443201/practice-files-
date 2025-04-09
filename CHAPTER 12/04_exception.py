try:
    a =  int(input("hey,Enter the number:"))
    print(a)

except ValueError as v:
    print("heyyyyy")
    print(v)
    
except Exception as e:
    print(e)

print("thank you")    
