class BaseClass:

    def set_name(self,name):
        self.name = name




class SubClass(BaseClass):

    def welcome(self):
        print("welcome")

    def display(self):
        print("name:  "+self.name)


x = BaseClass()
y = SubClass()

y.welcome()
y.set_name("ziyana")
y.display()


