#reference_variable.attribute_name=value
class Mobile:
    pass

mob1=Mobile()
mob2=Mobile()

mob1.price=20000
mob1.brand="Apple"

mob2.price=3000
mob2.brand="Samsung"
#Attributes can be added to a class through a special function called __init__(). 
# We will discuss more about the syntax later. But for now, this is how the mobile class will look like with attributes in it.
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    m1=Mobile("Apple",20000)
    m2=Mobile("Samsung",3000)

#in the code, brand and price are the attributes. All objects of this class will now have these attributes automatically. Here mob1 is assigned “Apple” and 20000 as values for the attributes brand and price respectively.

#Note:The parameter names and attribute names need not match
#When we create an object, the special __init__() method inside the
# class of that object is invoked automatically. 
# This special function is called as a constructor.
#self is not a keyword. self refers to the current object being executed.
class Mobile:
    def __init__(self):
        print("Inside constructor")
mob1=Mobile()
