stack = []
def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
        e = stack.pop()
        print(f"removed element is {e}")
        print(stack)

while True:
    print("Select the Operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Invalid input !")