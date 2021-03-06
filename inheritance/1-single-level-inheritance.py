class Parent:
    def parent_method(self):
        print('This method is from parent class')

class Child(Parent):
    def child_method(self):
        print('This method is from child class')


child1 = Child()

child1.child_method()
child1.parent_method()
