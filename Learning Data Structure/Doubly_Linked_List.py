class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.nref
                
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref 
            while n is not None:
                print(n.data,"--->",end=" ")  
                n = n.pref     

    def insert_empty(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            print("Linked list is not empty")
        
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
           self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n 
        
    def add_after(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not found!")
            else:
                new_node = Node(data)             
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
                
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not found!")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref 
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node
                
    def delete_begin(self):
        if self.head is None:
            print("LL is empty,can't remove nodes!")
        elif self.head.nref is None:
            self.head = None
        else:
            self.head = self.head.nref
            self.head.pref = None
            
    def delete_end(self):
        if self.head is None:
            print("LL is empty,can't remove nodes!")
        elif self.head.nref is None:
            self.head = None
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            n.nref = None
            
    def delete_by_value(self,x):
        if self.head is None:
            print("LL is empty,can't remove nodes!")
        elif self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print("Node is not found!")
        elif self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not found!")
            else:
                if n.nref is None:
                    n.pref.nref = None
                else:
                    n.pref.nref = n.nref
                    n.nref.pref = n.pref
                
                
                    

dLL1 = DoublyLinkedList()
dLL1.insert_empty(10)
dLL1.add_begin(16)
dLL1.add_end(26)
dLL1.add_after(245,10)
dLL1.add_before(300,245)
dLL1.delete_begin()
dLL1.delete_end() 
dLL1.delete_by_value(245)
dLL1.print_LL()
dLL1.print_LL_reverse()