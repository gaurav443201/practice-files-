p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 =  "click this"

message = input("Enter your COMMENT: ")

if((p1 in message) or (p2 in message) or (p3 in  message) or (p4 in message)):
    print("this comment is the spam")

else:
    print("this comment is not a spam")