class Animal:
    def __init__(self, name="unknow", feets=0):
        self.name = "Bobby"
        self.feets = 2

    def run(self):
        print("Let's run!")
        print("My name is : " + self.name)

class Dog(Animal):
    def __init__(self, name="unknow", feets=4, color="white"):
        super().__init__(name, feets)
        self.color = color

    def bark(self):
        print("Bark ！！！")

    def run(self):
        print(self.name + " is running")


littleDog = Dog()
littleDog.bark()
littleDog.run()