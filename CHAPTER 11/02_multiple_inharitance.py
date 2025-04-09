class Employee:
    company = "ICT"
    name = "mota bhai"
    def show(self):
        print(f"the name of the Employee is {self.name}")

class coder:
    language = "python"
    def printlanguage(self):
        print(f"out of all the language here is your language:{self.language}")    

class programmer(Employee,coder):
    company = "BHASAD"
    def showlanguage(self):
        print(f"the name is {self.company} and he is working in {self.company} company. he is good with {self.language} language")


a = Employee()
b = programmer()

b.show()
b.printlanguage()
b.showlanguage()