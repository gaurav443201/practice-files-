n : int=5

name: str= "gaurav"

def sum(a:int,b:int):
    return a+b
a=1
b=2
sum(a,b)

# Variable type hint 
age: int = 25 
# Function type hints 
def greeting(name: str) -> str: 
    return f"Hello, {name}!" 
# Usage 
print(greeting("Alice")) 