#for reading whole lines

f = open("file.txt")
lines = f.readlines()

print(lines,type(lines))

f.close()
print("--------------------------------------------------------------------------------------------------------------------")
#for  reading all lines one by one

f = open("file.txt")

line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
line3 = f.readline()
print(line3, type(line3))
line4 = f.readline()
print(line4, type(line4))
line5 = f.readline()
print(line5, type(line5))
print(line5=="")

print("_______________________________________________________________________________________________________")

f = open("file.txt")
line = f.readline()
while(line !=""):
    print(line)
    line= f.readline()

f.close