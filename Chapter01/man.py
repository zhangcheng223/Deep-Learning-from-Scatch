class man:
    def __init__(self,name):
        self.name = name
        print("Initialized")

    def hello(self):
        print("Hello "+self.name+"!")

    def goodbye(self):
        print("Good-bye "+self.name+"!")

m = man("David")
m.hello()
m.goodbye()
