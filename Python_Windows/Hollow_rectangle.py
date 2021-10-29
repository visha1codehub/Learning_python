n = int(input("Enter your number:"))
for i in range (n):
    for j in range (n):                                 #For diagonals
        if (i==0) or (j==0) or (i==n-1) or (j==n-1) or (i-j==0) or (i+j==n-1):
            print("*",end="")
        else:
            print(end=" ")

    print()
    
