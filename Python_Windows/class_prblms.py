class A :
    def print_str(self):
        print("This is method from class A ")
    # pass
class B(A):
    def print_str(self):
        print("This is method from class B ")
    pass
class C(A):
    def print_str(self):
        print("This is method from class C ")
    pass
class D(B,C):
    def print_str(self):
        print("This is method from class D ")
    pass

a = A()
b = B()
c = C()
d = D()

d.print_str()
