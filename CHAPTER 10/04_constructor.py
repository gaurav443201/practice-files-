class Employee:
    language = "python" #this is a class attribute 
    salary = 12000000

    def __init__(self, name, language,salary ): #this double under score method are called dunder method
        self.name = name
        self.language = language
        self.salary = salary 
        print("I am creating an object") #dunder method which automatically called

    def getInfo(self):
        print(f"The language is {self.language}. The salary {self.salary}")

    def greet(self):
        print("good morning") 

harry = Employee("harry", 13000000, "javascript")
harry.name = "harry"
print(harry.name , harry.salary )