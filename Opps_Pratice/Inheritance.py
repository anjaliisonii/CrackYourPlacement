#Is-a relationship is known as the inheritence
#The class which is inheriting is called the child/sub/derived class
#the class which is getting inherited is called the parent/super/base class
class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

FeaturePhone(10000,"Apple","13px").buy()
'''When we have a inheritance relationship, the attributes and behaviors get inherited,
 just like a child inherits certain attributes and behaviours from its parent. '''
'''From a code perspective, a child class inherits:

Constructor
Non Private Attributes
Non Private Methods'''
#Single Inheritence
#Single inheritance enables a derived class to inherit properties and behavior from a single parent class.
#Parent---Child
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()
#Multi-level Inheritence
#If a class is derived from another derived class then it is called multilevel inheritance.
#Grandfather---father----child
class Product:
    def review(self):
        print ("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()
###Heirarchiral 
#one parent---many childrens
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class SmartPhone(Phone):
    pass

class FeaturePhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()

#Multiple level-
#one children---many parents
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

    def return_phone(self):
        print ("Returning a phone")

class Product:
    def review(self):
        print ("Customer review")

class SmartPhone(Phone, Product):
    pass

s=SmartPhone(20000, "Apple", 12)

s.buy()
s.review()
#Contradiction
'''When a child is inheriting from multiple parents, 
and if there is a common behavior to be inherited, 
it inherits the method in Parent class which is first in the list. 
In our example, the buy() of Product is inherited as it appears first in the list.

 '''

 