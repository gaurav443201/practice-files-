a = int(input("enter the number :"))
b=  int(input("enter the second number:"))

if b==0:
    raise ZeroDivisionError("hey this program is not meant to divide number by zero")
else:
    print(f"The division a/b is {a/b}")
