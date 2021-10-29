
l = [1,2,3,4,5,6,7,8,97,6,4,3,2,3,56,7]
lis = list(map(lambda x:x**2,l))
print(lis)

def is_prime(y):
    for i in range(2,y):
        if (y%i == 0):
            return False
    else:
        return True       
lis1 = list(filter(is_prime,l))
print(lis1)