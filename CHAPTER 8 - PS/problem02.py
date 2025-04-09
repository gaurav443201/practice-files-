def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter the temperature in F:"))
print(f"{f_to_c(f)} °C")

#we can do it by this way also
c = f_to_c(f)
print(f"{round(c,2) }°C")