class Animal:
    def __init__(self, legs):
        print("Animal object was created")
        self._legs = legs
        self.runs = False

    def isRunning(self):
        self.runs = True
        print(f"Running started on {self._legs} legs")

    def count_legs(self):
        print(f"It has {self._legs} legs")

    def return_legs(self):
        return self._legs

cat = Animal(4)
cat.isRunning()
print(cat._legs)

class Dog(Animal):
    def __init__(self, legs, name):
        super().__init__(legs)
        self.name = name

    def dog_name(self):
        return self.name
    
    def bark(self):
        print('Bark!!!')

dog = Dog(4, 'Henry')
print(dog.dog_name())
dog.bark()
dog.count_legs()