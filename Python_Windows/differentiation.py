def main():

    n = int(input("Enter the power of x: "))
    formula = str(n)+"x**"+str(n-1)
    if n == 0:
        print(f"Differentiation of x to the power {n} is: 0")
    elif n == 1:
        print(f"Differentiation of x to the power {n} is: 1")
    else:
        print(f"Differentiation of x to the power {n} is: {formula}")
    
    FR = input("For continue press enter and for exit type any alphabate and then press enter.")
    if FR == '':
        main()
    else:
        exit()
main()