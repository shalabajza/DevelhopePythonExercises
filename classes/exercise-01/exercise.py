class Animal:
    def __init__(self, legs):
        print("Animal object was created")
        self.legs = legs
        self.runs = False

    def isRunning(self):
        self.runs = True
        print("Running started")

cat = Animal(4)
cat.isRunning()