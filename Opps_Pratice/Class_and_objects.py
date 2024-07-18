#Python is versaltile programmings langauage that supports oops
#through the used of objects and classed
#Object have attributes and behaviours 
#attributes - name, age, color, etc.
#behavior - dancing, singing, etc.
#Object:An object is simply a collection of data (variables) and methods (functions). 
# Similarly, a class is a blueprint for that object.
#An object is called an instance of a class.
#A class is considered a blueprint of objects.
#We can think of the class as a sketch (prototype) of a house
class Parrot:
    name=""
    age=0
p1=Parrot()
p1.name="Pihu"
p1.age=10
p2=Parrot()
p2.name="Mithu"
p2.age=12
print(f"{p1.name} is {p1.age} years old")
print(f"{p2.name} is {p2.age} years old")
