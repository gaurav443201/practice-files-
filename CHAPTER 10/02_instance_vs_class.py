class Employee:
    language = "python" #this is a class attribute  
    salary = 12000000

harry = Employee()
harry.language = "JavaScript"    #this is instance attribute 
print(harry.language, harry.salary)
#pahile instance attribute ka print hoga pra agar instance attribute na ho toh class attribute hi print hoga