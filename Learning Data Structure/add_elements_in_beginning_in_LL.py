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

LL1 = LinkedList()
LL1.add_begin('QWER')
LL1.add_begin('ZXCF')
LL1.add_begin('LKOI')
LL1.add_begin('HGFU')
LL1.add_begin('CVBN')
LL1.add_begin('ASFS')

LL1.print_LL()





                