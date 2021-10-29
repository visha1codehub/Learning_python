num = int(input("Enter your row no. :"))
for i in range(num):
     print(" " * (num-i-1),end='')
     print("*" * (2*i + 1),end='')
     print(" " * (num-i-1))


 # Another way to print this pattern
num = int(input("Enter your row no. :"))
for i in range(1,num+1):
     print(" "*(num-i)+"* "*i)

# One more way
num = int(input("Enter your row no. :"))
for i in range (0,num):
    for j in range (0,num-i-1):
        print(" ",end="")
    for k in range (0,i+1):
        print("* ",end="")
    print()
