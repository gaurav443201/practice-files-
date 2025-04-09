f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("the word 'twinkle' is present in this content")
else:
    print("the word 'twinkle' is not present in this content")

f.close()