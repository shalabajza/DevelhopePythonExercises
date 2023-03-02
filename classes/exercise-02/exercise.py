class Animal:
    def __init__(self, legs):
        print("Animal object was created")
        self.legs = legs
        self.runs = False

    def isRunning(self):
        self.runs = True
        print("Running started")

    def count_legs(self):
        print(f"It has {self.legs}")

    def return_legs(self):
        return self.legs

cat = Animal(4)
cat.isRunning()
print(cat.legs)