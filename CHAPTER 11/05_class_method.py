class Employee:
    a =1

    def show(self):
        print(f"the class value of a is {self.a}")

e = Employee()

e.a = 45

e.show()
print("------------------------------------------------------------------------------------------------")
class Employee:
    a =1

    @classmethod 
    def show(cls):
        print(f"the class value of a is {cls.a}")

e = Employee()

e.a = 45

e.show()