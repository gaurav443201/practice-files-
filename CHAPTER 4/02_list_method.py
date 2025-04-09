from typing import Iterable


friends = ["Apple", "Orange", 5, 345.56, False, "Akash","Rohit"]

print(friends)

friends.append("Harry")

print(friends)

l1 = [1, 34,62, 2, 6, 11]
l1.sort()
print(l1)

l2 = [1, 34,62, 2, 6, 11]
l2.reverse()
print(l2)

l3 = [1, 34,62, 2, 6, 11]
l3.insert(3,3333)  # insert 3333 such that its index in the list is 3
print(l3)

l4 = [1, 34,62, 2, 6, 11]
l4.pop(3)
print(l4)
# OR

l5 = [1, 34,62, 2, 6, 11]
value = l5.pop(3) 
print(value)
print(l5)

l6 = [1, 34,62, 2, 6, 11]
l6.remove(6)
print(l6)

l7 = [1, 34,62, 2, 6, 11]
l7.clear()
print(l7)

l8 = [1, 34,62, 2, 6, 11]
l8.count(2)
print(l8)

l9 = [1, 34,62, 2, 6, 11]
l9.copy()
print(l9)