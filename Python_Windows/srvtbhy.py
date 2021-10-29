# f = open("pr4.py","r")
# a = f.read()
# print(a)
# f.close()

#Exercise
l1 = ['aloo','bhindi','baigan','gazar','muli','khira']

i = 1
for item in l1:
    if i%2 != 0:
        print(f"{item}")
    i += 1
    
import random 
counter = True

def game (a,b):
    return a+b*random.randint(23,67)

s = game(23,56)
print(s)

