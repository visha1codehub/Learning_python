def greatest(x,y,z):
    if x>y:
        f1 = x
    else:
        f1 = y
    if y>z:
        f2 = y
    else:
        f2 = z
    if f1 > f2:
        return f1
    else:
        return f2


c = greatest(int(input("1st: ")),int(input("2nd: ")),int(input("3rd: ")))
print(c)
