class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild :
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild :
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)  
        
    def search(self,data):
        if self.key is None:
            print("Tree is empty!")
            return
        if self.key == data:
            print("Node is Found!")
            return
        if self.key > data:
            if self.lchild :
                self.lchild.search(data)
            else:
                print("Node is not present in the tree!")
        else:
            if self.rchild :
                self.rchild.search(data)
            else:
                print("Node is not present in the tree!")
     
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()           
        if self.rchild:
            self.rchild.preorder() 
        
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()           
        print(self.key,end=" ")          
        if self.rchild:
            self.rchild.inorder()
            
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()          
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")
            
    def delete(self,data):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not present in the tree!")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not present in the tree!")  
        
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print(f"Node with smallest key is {current.key}.")
        
    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print(f"Node with largest key is {current.key}.")
    
          
root = BST(10)
list1 = [20,31,8,6,5,23,98,76,45,98,23,12,56,63,0]
for i in list1:
    root.insert(i)
# root.search(12)
# print("Preorder")
# root.preorder()
# print()
# print("Inorder")
# root.inorder()
# print()
# print("Postorder")
# # root.postorder()
# print("After deleting!")
root.delete(10)
root.preorder()
root.min_node()
root.max_node()
 