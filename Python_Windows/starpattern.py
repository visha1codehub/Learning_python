for i in range(1,8):
    for j in range(1,10):
        if ((i == 1 or i == 7) and j == 5) or ((i == 2 or i == 6) and (j == 4 or j == 6)) or ((i == 3 or i == 5) and j%2 != 0) or (i == 4 and (j == 2 or j == 8)) :
            print("*",end="")
        else:
            print(end=" ")
    print()