class programmer:
    company = "microsoft"
    def __init__(self, name, salary ,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p= programmer("harry", 1200000, 443201)
print(p.name, p.salary, p.pin, p.company)        
r= programmer("rohan", 2200000, 440001)
print(r.name, r.salary, r.pin, r.company)        
s= programmer("shubham", 9000000, 442121)
print(s.name, s.salary, s.pin, s.company)        
      
      
        