def main():

    n = int(input("Enter the power of x: "))
    formula = 'x**'+str(n+1)+"/"+str(n+1)
    if n == 0:
        print(f"integration of x to the power {n} is: x")
    elif n == -1:
        print(f"integration of x to the power {n} is: log(x)")
    else:
        print(f"integration of x to the power {n} is: {formula}")
    
    FR = input("For continue press enter and for exit type any alphabate and then press enter.")
    if FR == '':
        main()
    else:
        exit()
main()