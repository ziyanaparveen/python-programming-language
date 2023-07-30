class Sample:
    def set_name(self,name):
        self.name = name
        print(name)


    def __add__(self, other):
        name = self.name+other.name
        return name




first_name = Sample()
second_name = Sample()

first_name.set_name("ziyana")
second_name.set_name("parveen")

full_name = first_name+second_name
print(full_name)