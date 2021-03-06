class A:
    def A_method(self):
        print('This method belongs to class A')

class B:
    def B_method(self):
        print('This method belongs to class B')

class C(A,B):
    def C_method(self):
        print('This method belongs to class C')


c = C()

c.A_method()
c.B_method()
c.C_method()