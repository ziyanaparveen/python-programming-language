class First:
    def display(self):
        print("First")

class Second():
    def display(self):
        print("Second")

#itwill print third and second
#class Third(Second,First):

class Third(First,Second):
    def display_third(self):
        print("Third")

x = Third()
x.display_third()
x.display()

print(Third.mro())
