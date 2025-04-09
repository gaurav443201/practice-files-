# old.txt delete ho jaye aur renamed_by_python.txt banke 
import os
file_path = "old.txt"
os.remove(file_path)

with open("old.txt") as f:
    content =  f.read()
with open("renamed_by_python.txt", "w"):
    f.write(content)    