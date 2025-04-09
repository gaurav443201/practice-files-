def get_length(s):
    print("Length of string:", len(s))

def reverse_string(s):
    print("Reversed string:", s[::-1])

def check_equality(s1, s2):
    if s1 == s2:
        print("Strings are equal")
    else:
        print("Strings are not equal")   

def check_palindrome(s):
    if  s == s[::-1]:
        print("String is palindrome")
    else:
        print("String is not palindrome")

def check_substring(s, sub):
    print("Substring found:", sub in s)

print("String Operations Menu:")
print("1. Check length of string")
print("2. Reverse of string")
print("3. Equality check of two strings")
print("4. Check palindrome")
print("5. Check substring")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    s = input("Enter the string: ")
    get_length(s)
elif choice == 2:
    s = input("Enter the string: ")
    reverse_string(s)
elif choice == 3:
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    check_equality(s1, s2)
elif choice == 4:
    s = input("Enter the string: ")
    check_palindrome(s)
elif choice == 5:
    s = input("Enter the main string: ")
    sub = input("Enter substring: ")
    check_substring(s, sub)
else:
    print("Invalid choice! Please enter a number between 1 and 5.")
