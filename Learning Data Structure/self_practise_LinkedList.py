class Node:
    def __init__(self,data):
        self.data = data 
        self.ref = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
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
            
    def add_after(self,data,x):   
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not found!")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
            
    def add_before(self,data,y):
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
            
    def add_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty!")
            
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty ,can't remove nodes!")
        else:
            self.head = self.head.ref
            
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty, can't remove nodes!")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
            
    def delete_by_value(self,x):
        if self.head is None:
            print("Linked list is empty, can't remove nodes!")
        elif self.head.data == x:
            self.head = self.head.ref
        else:
            n = self.head
            while n is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n is None:
                print("Node is not found!")
            else:
                n.ref = n.ref.ref
            
LL1 = LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(60)
LL1.add_begin(50)
# LL1.add_end(30)
# LL1.add_end(110)
# LL1.add_end(160)
# LL1.add_after(40,10)
# LL1.add_before(70,110)
# LL1.add_empty(80)
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_by_value(50)
LL1.print_LL()

