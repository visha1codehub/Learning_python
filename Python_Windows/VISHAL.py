for i in range (7):
    for j in range (13):
        if (i-j==0) or (i+j==12):
            print("*",end="")
        else:
            print(end=" ")

    for j in range (7):
        if (i==0) or (i==6) or (j==3):
            print("*",end="")
        else:
            print(end=" ")

    for j in range (7):
        if (((i==0) or (i==3) or (i==6)) and ((j>0) and (j<6))) or ((j==0) and ((i>0) and (i<3))) or ((j==6) and ((i>3) and (i<6))):
            print("*",end="")
        else:
            print(end=" ")

    for j in range (7):
        if (j==0) or (j==6) or (i==3):
            print("*",end="")
        else:
            print(end=" ")

    for j in range (7):
        if (((j==0) or (j==6)) and (i!=0)) or (i==3) or ((i==0) and ((j>0) and (j<6))):
            print("*",end="")
        else:
            print(end=" ")

    for j in range (7):
        if (j==0) or (i==6):
            print("*",end="")
        else:
            print(end=" ")
    print()


