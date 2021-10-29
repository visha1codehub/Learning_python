
def is_prime(num):
    
    if num == 1:
        print("1 is neither Prime nor Composite.")
    else:
        if num > 1:
            for i in range (2,num):
                if (num % i == 0):
                    print("This number is not Prime.")
                    break
            else:
                print("This number is Prime.")
        else:
            print("Negavite numbers cannot be Prime.")


if __name__ == '__main__':
    a = int(input("Enter your number: "))
    is_prime(a)







