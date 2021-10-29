class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref 

LL1 = LinkedList()
LL1.print_LL()