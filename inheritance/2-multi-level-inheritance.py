class Grandparent:
    def grandparent_method(self):
        print('This method is from grandparent class')

class Parent(Grandparent):
    def parent_method(self):
        print('This method is from parent class')

class Child(Parent):
    def child_method(self):
        print('This method is from child class')


parent1 = Parent()
child1 = Child()


parent1.grandparent_method()

print('---')
child1.parent_method()
child1.grandparent_method()