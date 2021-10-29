import random

def main():
    a = input("For roll the dice type 'r'. ")
        
    if a == 'r':
        dice_No = random.randint(1,6)
        print(f'Your output number on dice is {dice_No}.')

        b = input("Do you wanna roll the dice again,  y/n? ")
        if b == 'y':
            main()
        else:
            print("Byyy")
            exit()
        
    else:
        print("You entered invalid input! Enter correct input.")
        main()
        

main()