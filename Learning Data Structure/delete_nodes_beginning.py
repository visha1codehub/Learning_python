class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.ref
                
    def add_begin(self,data):
        new_node = Node(data) 
        new_node.ref = self.head
        self.head = new_node
        
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty so you cannot delete any node!")
        else:
            self.head = self.head.ref 
            
    

LL1 = LinkedList()
LL1.add_begin(100)
LL1.add_begin(200)
LL1.add_begin(500)
LL1.add_begin(800)
LL1.delete_begin()
LL1.print_LL()





                