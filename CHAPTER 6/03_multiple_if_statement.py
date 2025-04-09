a = int(input("Enter your age: "))

#if statement no.1
if(a%2 ==0):
    print("a is even")
#end of if statement no. 1 

#if statement no.2
if(a>=18):
    print("You are above the age of consent")
    print("good for you")
elif(a<0):
    print("you are entering invalid age")
else:
    print("you are below the age of consent")

#end of if statement no.2
print("end the program")    