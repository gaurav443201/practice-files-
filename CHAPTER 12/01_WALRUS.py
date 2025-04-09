#using walrus operator
if (n:=len([1,2,3,4,5])) > 3:
    print(f"list is too long ({n} element, <=3 ) ")

#output :list is too long (5 element, <=3 )     