class BaseClass:
    def display(self):
        print("hello")




class SubClass(BaseClass):
    def welcome(self):
        print("welcome")


x = BaseClass()
y = SubClass()
x.display()
y.display()
y.welcome()