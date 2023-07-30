class MyBcaMembers:
    year = 2020
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age+1

    def relocate(self,place):
        self.place = place

    @classmethod
    def add_year(cls):
        cls.year = cls.year+1

    def display(self):
        print("year: "+str(MyBcaMembers.year))
        print("name: " +self.name )
        print("age: " +str(self.age ))
        print("place: " +self.place )


x = MyBcaMembers("zzi",24,"pookom")
y = MyBcaMembers("sithu",24,"panoor")

x.display()
y.display()

x.add_year()
y.add_year()
x.add_age()
y.add_age()
x.relocate("bhrain")
y.relocate("kozhikode")
x.display()
y.display()


