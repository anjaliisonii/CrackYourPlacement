#Creating the simple class
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return f"{self.name} says hello!"
# dog=Animal("charlie")
# print(dog.speak())


#Creating sub class
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} says hello!!"
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!!"
dog=Dog("Charlei")
print(dog.speak())