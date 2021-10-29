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
        
    def add_end(self,data):
        new_node = Node(data) 
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
            
    def add_before_node(self,data,y):
        if self.head is None:
            print("Linked list is empty!")
            return
        if self.head.data == y:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == y:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
            
        

LL1 = LinkedList()
LL1.add_end(10)
LL1.add_end(200)
LL1.add_end(30)
LL1.add_before_node(40,10)
LL1.add_before_node(70,10)
LL1.print_LL()





                