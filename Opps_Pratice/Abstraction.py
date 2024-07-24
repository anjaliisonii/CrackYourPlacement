class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        pass
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        return "Boo boo"
class Cat(Animal):
    def sound(self):
        return "Meow"
class Dear(Animal):
    def sound(self):
        return "Hoo"
d1=Dog("Buddy")
print(d1.name)
print(d1.sound())


from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
 
class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")
 
class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")
 
#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)
 
#object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)
 
print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass?)
      

