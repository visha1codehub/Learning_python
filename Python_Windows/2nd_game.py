# Rock_Paper_Scissor game
import random         

counter = True

def RPS_game(comp,you):
        if you == comp:
            return None
        elif you == 'r':
            if comp == 'p':
                return False
            elif comp == 's':
                return True
        elif you == 'p':
            if comp == 's':
                return False
        elif you == 's':
            if comp == 'r':
                return False
            elif comp == 'p':
                return True

while counter == True:            
    your_choice = input("Your turn: Rock(r) Paper(p) or Scissor(s)?").lower()
   
    # Check for valid input
    if your_choice == 'r' or your_choice == 'p' or your_choice == 's':    
        random_No = random.randint(1,3)
        if random_No == 1:
            comp_choice = 'r'
        elif random_No == 2:
            comp_choice = 'p'
        elif random_No == 3:
            comp_choice = 's'

        a = RPS_game(comp_choice,your_choice)

        print(f"You chose {your_choice}")
        print(f"Computer chose {comp_choice}")
        if a == None:
            print("Game is Tie.")
        elif a:
            print("You won.")
        else:
            print("You lost.")

        for_repeat = input("Do you wanna continue this game? y/n:").lower()
        if for_repeat == 'y':
            continue
        else:
            exit()
    else:
        print("Your choice is not valid ! Please enter valid choice.")
        continue    