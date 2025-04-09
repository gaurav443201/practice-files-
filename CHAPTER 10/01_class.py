class Employee:
    language = "python"  #this is class attribute
    salary = 12000000

harry = Employee()
harry.name = "Harry"  #this is object attribute   
print(harry.name ,harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan"     
print(rohan.name ,rohan.language,rohan.salary)

# here name is the object attribute and salary and language are class attribute as they directly belong to the class