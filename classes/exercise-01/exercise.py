class Animal:
    def __init__(self, legs):
        self.legs = legs
        self.runs= False

    def isRunning(self):
        self.runs = True
        print("Running...")

cat = Animal(4)
cat.isRunning()