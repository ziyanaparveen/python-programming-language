class MainClass:
    def __init__(self):
        print("MainClass init")

    def set_name(self,name):
        self.name = name
        print("base class set name")





class SubClass(MainClass):

    def __init__(self):
        print("SubClass init")


    def display(self):
        print("ziyana")
        print("name: "+self.name)

    def set_name(self, name):

#to call function from main class in case of method overriding
        super().set_name(name)

        self.name = name
        print("sub class set name")





x = MainClass()
y = SubClass()


y.set_name("sithu")
y.display()