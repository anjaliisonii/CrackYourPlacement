class Animal:
    def __init__(self, name,breed):
        self.name = name
        self.breed=breed

    def speak(self):
        return f"{self.breed} says hello!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name,breed)
        self.breed = breed

dog = Dog("Charlie", "Bulldog")
print(dog.speak())
print(dog.breed)