def right(a,b,c):
    sides=sorted([a,b,c])
    return sides[0]**2+sides[1]**2==sides[2]**2
a=int(input("side 1:"))
b=int(input("side 2:"))
c=int(input("side 3:"))

if right(a,b,c):
    print("It is a right angled triangle")
else:
    print("It is not a right angled triangle")