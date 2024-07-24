#Here are encapsulation so we are acccesing it by the preventing (Access Modifier)
#Just the way a lock prevents others from accessing your property, 
#we can restrict other parts of the code from directly accessing sensitive data.
#Public Data Access
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance

    def update_balance(self,amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount

    def show_balance(self):
            print("The balance is ",self.wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
#Private Data Access
'''We can put a lock on that data by adding a double underscore in front of it, as shown in below code.
Adding a double underscore makes the attribute a private attribute. 
Private attributes are those which are accessible only inside the class. This method of restricting access to our data is called encapsulation.'''
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance += amount

    def show_balance(self):
        print ("The balance is ",self.__wallet_balance)

c1=Customer(100, "Gopal", 24, 1000)
print(c1.__wallet_balance)

#if we want to update the varible then use the ClassName for that
# c1=Customer(100, "Gopal", 24, 1000)
# c1._Customer__wallet_balance = 10000000000
# c1.show_balance()
#So Encapsulation is bassically not accesing it is alert Sign to not use it directly
##########################################################################
'''To have a error free way of accessing and updating private variables, we create specific methods for this.

The methods which are meant to set a value to a private variable are called setter methods
The methods meant to access private variable values are called getter methods
The below code is an example of getter and setter methods:'''
class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    #It is Know as the Mutator method
    def set_wallet_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.__wallet_balance = amount
    #It is Know as the Accessor method
    def get_wallet_balance(self):
        return self.__wallet_balance

c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())


#Encapsulation is the fundamental concept of object oriented programming that invovle 
#budling of data(atrrubute) and method into the the single unit called class .
#It allows us to hide the internal state of a object and restrist from the accidencal modification
#Encapsulation promotes the principle of data hiding and information hiding, which are essential for building robust and maintainable software systems.
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if age>0:
            self._age=age
        else:
            print("age must be positive")
p1=Person("Anjali",30)
print(p1._Person__name)
print(p1.get_age())
print(p1.get_name())




# class Vehicle:

#     def __init__(self,vehicle_cost,vehicle_type,vehicle_id,premi_account):
#         self.__vehicle_cost=vehicle_cost
#         self.__vehicle_type=vehicle_type
#         self.__vehicle_id=vehicle_id
#         self.__premi_account=premi_account
#     def calculate_premium(self):
#         if self.__vehicle_type=="Two Wheeler":
#             self.__premi_account=(2/100)*self.__vehicle_cost
#             return self.__premi_account
#         if self.__vehicle_type=="Four Wheeler":
#             self.__premi_account=(6/100)*self.__vehicle_cost
#             return self.__premi_account
#         else:
#             print("Invalid")
#     def set_vehicle_type(self,vehicle_type):
#         self.__vehicle_type=vehicle_type
#     def set_vehicle_id(self,vehicle_id):
#         self.__vehicle_id=vehicle_id
#     def set_vehicle_cost(self,vehicle_cost):
#         self.__vehicle_cost=vehicle_cost
#     def set_premi_account(self,premi_account):
#         self.__premi_account=premi_account
#     def get_vehicle_type(self):
#         return self.__vehicle_type
#     def get_vehicle_id(self):
#         return self.__vehicle_id
#     def get_vehicle_cost(self):
#         return self.__vehicle_cost
#     def get_premi_account(self):
#         return self.__premi_account
        
#     def display_vehicle_details(self):
#         print(self.__vehicle_cost,self.__premi_account,self.__vehicle_type,self.__vehicle_id)
# v1=Vehicle(90000,"Four Wheeler",15,0)
# v1.set_vehicle_id(10)
# v1.set_vehicle_type("Four Wheeler")
# v1.set_vehicle_cost(6768878)
# v1.calculate_premium()
# v1.display_vehicle_details()