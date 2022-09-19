x = int(input())
y = int(input())
z = int(input())
a = int(input())

if a>x>y>z or a>y>z>x or a>z>x>y or a>x==y==z or a>x>z>y or a>y>x>z or a>z>y>x:
    if x>y>z or y>x>z or x==y>z:
        print(a*z)
    elif y>z>x or z>y>x or z==y>x:
        print(a*x)
    elif x>z>y or z>x>y or z==x>y:
        print(a*y)
elif x>a>y>z or x>y>z>a or x>z>a>y or x>a==y==z or x>a>z>y or x>y>a>z or x>z>y>a:
    if a>y>z or y>a>z or a==y>z:
        print(x*z)
    elif y>z>a or z>y>a or z==y>a:
        print(a*x)
    elif a>z>y or z>a>y or z==a>y:
        print(x*y)
elif y>x>a>z or y>a>z>x or y>z>x>a or y>x==a==z or y>x>z>a or y>a>x>z or y>z>a>x:
    if x>a>z or a>x>z or x==a>z:
        print(y*z)
    elif a>z>x or z>a>x or z==a>x:
        print(y*x)
    elif x>z>a or z>x>a or z==x>a:
        print(a*y)
elif z>x>a>y or z>a>y>x or z>y>x>a or z>x==a==y or z>x>y>a or z>a>x>y or z>y>a>x:
    if x>a>y or a>x>y or x==a>y:
        print(y*z)
    elif a>y>x or y>a>x or y==a>x:
        print(z*x)
    elif x>y>a or y>x>a or y==x>a:
        print(a*z)
