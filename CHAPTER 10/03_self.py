class Employee:
    language = "python" #this is a class attribute  
    salary = 12000000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is  {self.salary} ")

    def greet(self): #we can remove the self from it and make it static
        print("good morning")
harry = Employee()
harry.language = "JavaScript"    #this is instance attribute 
#print(harry.language, harry.salary)

harry.getInfo()
# Employee.getInfo(harry)
harry.greet()