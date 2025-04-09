post = input("Enter the post: ")

"""if("Harry" in post ):
    print("This post is talking about Harry")""" #yah agar hamne haRRy aisa likha th ans nahi aayeega

if("Harry".lower() in post.lower() ):
    print("This post is talking about Harry") #but here is different
else:
    print("This post is not talking about Harry")    