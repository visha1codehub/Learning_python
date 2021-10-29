a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
d = int(input("Enter 4th number:"))
e = int(input("Enter 5th number:"))

if a>e:
    f1 = a
else:
    f1 = e

if b>d:
    f2 = b
else:
    f2 = d

if f2>c:
    f3 = f2
else:
    f3 = c

if f1>f3:
    print("The greatest number is",f1)
else:
    print("The greatest number is",f3)
    