class Parent:
    def __init__(self):
        print('Parent class init function')
    def parent_method(self):
        print('This method is from parent class')

# class Child(Parent):
#     def child_method(self):
#         print('This method is from child class')

# child = Child() #Executes Parent init function


class Child2(Parent):
    def __init__(self):
        super().__init__()
        print('Child class init function')

child2 = Child2() # Executes Child init function













# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('Child class init function')
#     def child_method(self):
#         print('This method is from child class')


# class Grandchild(Child):
#     def __init__(self):
#         super().__init__()
#         print('Grandchild class init function')
    
# grandchild = Grandchild()