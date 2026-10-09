# Accept the name and check if it's a palindrome
name = input("Enter a name: ")

if name == name[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")