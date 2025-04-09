marks  = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

print(marks.items())
print(marks.keys())


marks.update({"Harry": 99, "Mahesh" : 100})
print(marks)

print(marks.get("Harry"))
print(marks.get("Tushar"))

# what is the difference between 
# print(marks["Harry"])  and   print(marks.get("Harry2"))

# if we write print(marks["Harry2"]) it will give us error
# but if we print(marks.get("Harry2")) then it will give us none not an error
