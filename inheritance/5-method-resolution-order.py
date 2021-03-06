class A:
    def __init__(self):
        print('Class A init')
    
    def generic_method(self):
        print('Method from A')

class B:
    def __init__(self):
        print('Class B init')
    
    def generic_method(self):
        print('Method from B')

class C(B,A):
    def __init__(self):
        super().__init__()
        print('Class C init')


c1 = C()

c1.generic_method()