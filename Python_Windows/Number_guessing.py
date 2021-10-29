import random

def main():
    try:
        comp_choice = random.randint(1, 10)
        random_num = random.randint(2,6)
        your_1stchoice = int(input("Guess the number.\nHint:The number is between 1 to 10.--"))
        if your_1stchoice in range(1, 11):
            if your_1stchoice == comp_choice:
                print("Congrates! You guess the correct number.\nAnd your score is 100.")
            else:
                print("You guess the incorrect number.")
                print("Here is another clue: The number is multiple of",(comp_choice*random_num  ))
                your_2ndchoice = int(input("Guess the number: "))
                if your_2ndchoice == comp_choice:
                    print("Congrates! You guess the correct number.\nAnd your score is 50.")
                else:
                    print("You guess the incorrect number again.\nAnd you lost.")
                    print(f"Computer's number was {comp_choice}.")

                for_restart = input("Do you wanna continue this game? y/n: ")
                if for_restart == 'y':
                    main()
                else:
                    print("Bye!")
                    exit()
        else:
            print("Your entered number is out of range! Please enter a number in given range.")
            main()
    except ValueError:
        print("Not a valid number, please enter a valid number !")
        main()
 
main()
