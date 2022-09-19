x = int(input())
y = int(input())
z = int(input())

if x>y>z or y>x>z or x==y>z:
    print(z)
elif y>z>x or z>y>x or z==y>x:
    print(x)
elif x>z>y or z>x>y or z==x>y:
    print(y)
