
for r in range (7):
    for c in range(9):
        if (r==0 and c%4!=0) or (r==1 and c%4==0) or (r-c==2) or (r+c==10):
            print("*",end="")
        else:
            print(" ",end="")
    print()