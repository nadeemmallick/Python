x = int(input("Enter the first side of triangle :"))
y = int(input("Enter the second side of triangle :"))
z = int(input("Enter the third side of triangle :"))

if (x+y)>z and (y+z)>x and (z+x)>y:
    print("They are side of triangles")
else:
    print("Not side of triangle")

