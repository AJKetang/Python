class Animal:
    def __init__(self, name="unknow", feets=0):
        self.name = "Alex"
        self.feets = 2

    def run(self):
        print("Let's run!")
        print("My name is : " + self.name)


##Construct animal object: animalA##
animalA = Animal()
##print animalA's name
print(animalA.name)
##print animalA's feets
print(animalA.feets)
##Make animalA run
animalA.run()


