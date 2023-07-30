class MySampleClass:
    def hello(self, name):
        self.name = name
    def print_name(self):
        print(self.name)





x = MySampleClass()
y = MySampleClass()
name = "ziyA"
x.hello(name)
y.hello('sithu')

x.print_name()
y.print_name()