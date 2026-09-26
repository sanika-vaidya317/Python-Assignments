##To check if string contains only ASCII
s = input("Enter a string: ")
if all(('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') for c in s):
    print("The string contains only ASCII characters.")
else:
    print("The string contains non-ASCII characters.")