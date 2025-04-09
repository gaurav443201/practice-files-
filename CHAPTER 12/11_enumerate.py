l =[23,34,45,56,78,90]

index= 0 
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

print("\n")
#this can be simply written as  
for index,item in enumerate(l):
        print(f"The item number at index {index} is {item}") 