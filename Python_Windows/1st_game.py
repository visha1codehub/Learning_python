# Snake_Water_Gun game
import random
def Game(comp,you):
    if comp == you:
            return None
    elif comp == 's':
        if you == 'w':
                return False
        elif you == 'g':
                return True        
    elif comp == 'w':
        if you == 'g':
                return False
        elif you == 's':
                return True
    elif comp == 'g':
        if you == 's':
                return False
        elif you == 'w':
                return True



def main():
    you = input("your turn: Snake(s) Water(w) or Gun(g)?")
    if you == 's' or you == 'w' or you == 'g':

        randNO = random.randint(1,3)
        if randNO == 1:
            comp = 's'
        elif randNO == 2:
            comp = 'w'
        elif randNO == 3:
            comp = 'g'

        
        a = Game(comp,you)

        print(f'Computer chose {comp}')
        print(f'You chose {you}')
        if a == None:
            print("The game is tie.")
        elif a:
            print("You won the game.")
        else:
            print("You lost the game.")
        repeat = input("contiue or not?? y/n:")
        if repeat == 'y':
            main()
        else:
            exit()
    else:
        print("Your choice is not valid ! Please enter valid choice.")
        main()
main()

