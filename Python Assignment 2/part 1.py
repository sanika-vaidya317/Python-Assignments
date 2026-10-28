#input three nos
a=int(input("First no:"))
b=int(input("Second no:"))
c=int(input("Third no:"))

if a==b==c:
    print("All numbers are equal")
elif a==b and a>c:
    print("a and b and greatest")
elif a==c and a>b:
    print("a and c are greatest")
elif b==c and b>a:
    print("b and c are greatest")
elif a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")
    
