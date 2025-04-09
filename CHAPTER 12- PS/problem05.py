n = int(input("Enter the number: "))

table = [i*n for i in range(1,11)]

with open("tables.txt", "a") as f:
    f.write(f"table of {n} : {str(table)} \n" )
    


