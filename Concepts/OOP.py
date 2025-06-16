# OOP principles:
# 	1.	（Encapsulation）封装
# 	2.	（Inheritance）继承
# 	3.	（Polymorphism）多态
# 	4.	（Abstraction）抽象



# 1. Encapsulation

# Encapsulation is the practice of bundling data (attributes) and methods together while restricting direct access to certain parts of an object.
class Animal:
    def __init__(self, name, species):
        self.name = name  # Public attribute
        self.__species = species  # Private attribute (cannot be accessed directly) , you must know the name before access .

    def get_species(self):
        # Using public method to access the private attribute
        return self.__species

    def make_sound(self):
        # Method to be overridden by subclasses
        pass

# Creating an instance
lion = Animal("Simba", "Lion")

print(lion.name)  # ✅ Accessing public attribute -> Simba
# print(lion.__species)  # ❌ Cannot access private attribute directly
print(lion.get_species())  # ✅ Accessing private attribute via method -> Lion
# Key Points
# 	•	Private attributes (__species) cannot be accessed directly outside the class.
# 	•	Encapsulation protects data integrity by preventing unintended modifications.
# 	•	Public methods (get_species()) provide controlled access to private attributes.



# 2. Inheritance

# Inheritance allows a child class to inherit methods and properties from a parent class, reducing code duplication.
class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Calling the parent class constructor
        self.breed = breed  # Adding a new attribute

    def make_sound(self):
        # Overriding make_sound() method
        return "Woof! Woof!"

# Creating a subclass instance
dog = Dog("Buddy", "Golden Retriever")
print(dog.name)  # ✅ Inherited from Animal -> Buddy
print(dog.get_species())  # ✅ Inherited method -> Dog
print(dog.make_sound())  # ✅ Overridden method -> Woof! Woof!
# Key Points
# 	•	Dog class inherits from Animal, reusing attributes and methods.
# 	•	super().__init__() calls the parent class constructor to initialize name and species.
# 	•	make_sound() is overridden to define a specific behavior for Dog.



# 3. Polymorphism

# Polymorphism allows different classes to use the same method name but implement it differently.
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")  # Explicitly setting species to "Cat"

    def make_sound(self):
        # Overriding make_sound() method
        return "Meow! Meow!"

# Creating a list of different animal objects
animals = [Dog("Buddy", "Golden Retriever"), Cat("Whiskers")]

# Looping through each animal and calling make_sound()
for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}")
# Key Points
# •	Dog and Cat both inherit from Animal, but each implements make_sound() differently.
# •	We can treat different objects in a uniform way, reducing the need for specific conditions (if-else checks).


# 4. Abstraction(Honestly this is the most difficult for me to understand at first:) 

# Abstraction is the practice of hiding complex details and exposing only necessary features.
#It is achieved using abstract classes and abstract methods.
#Abstract classes act as blueprints that enforce certain methods in subclasses.
#Subclasses must implement the abstract methods (or they will also remain abstract).

# from abc import ABC, abstractmethod

# class Animal(ABC):  # Abstract base class (ABC)
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def make_sound(self):
#         # Abstract method that must be implemented in subclasses
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof! Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow! Meow!"

# # animal = Animal("Unknown")  # ❌ Cannot instantiate an abstract class
# dog = Dog("Buddy")
# print(dog.make_sound())  # ✅ Woof! Woof!



# Example 1: Payment System
from abc import ABC, abstractmethod

# Abstract class
class Payment(ABC):  
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method that must be implemented in all subclasses"""
        pass

# Concrete class: Credit Card payment
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

# Concrete class: PayPal payment
class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Example usage
def make_payment(payment_method: Payment, amount):
    payment_method.process_payment(amount)

# Creating instances of different payment methods
credit_card = CreditCardPayment()
paypal = PayPalPayment()

# Making payments
make_payment(credit_card, 100)  # Output: Processing credit card payment of $100
make_payment(paypal, 50)        # Output: Processing PayPal payment of $50




#Example 2 Vehicle System:
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        """Abstract method that must be implemented in subclasses"""
        pass

# Concrete class: Car
class Car(Vehicle):
    def move(self):
        print(f"{self.name} moves by driving on roads.")

# Concrete class: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print(f"{self.name} moves by pedaling.")

# Creating objects
car = Car("Toyota")
bike = Bicycle("Mountain Bike")

# Using the common interface
car.move()  # Output: Toyota moves by driving on roads.
bike.move()  # Output: Mountain Bike moves by pedaling.




# Example 3: Employee Salary Calculation
from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        """Abstract method that must be implemented in subclasses"""
        pass

# Concrete class: Full-Time Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# Concrete class: Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Creating instances
john = FullTimeEmployee("John", 5000)
alice = ContractEmployee("Alice", 20, 160)  # $20 per hour, 160 hours

# Calculating salaries
print(f"{john.name}'s Salary: ${john.calculate_salary()}")  # Output: John's Salary: $5000
print(f"{alice.name}'s Salary: ${alice.calculate_salary()}")  # Output: Alice's Salary: $3200


# Key Points
# 	•	Animal(ABC) is an abstract class, meaning it cannot be instantiated directly.
# 	•	Any subclass must implement     @abstractmethod, ensuring consistency.
# 	•	Abstraction simplifies usage by defining a common structure.



# Why Use OOP?

# ✅ Improves code readability: Encapsulation makes code more structured.
# ✅ Promotes code reuse: Inheritance avoids repetitive code.
# ✅ Enhances flexibility: Polymorphism makes the system extensible.
# ✅ Simplifies maintenance: Abstraction enforces consistency and reduces complexity.

# OOP is widely used in various applications such as:
# 	•	Game development (e.g., Player, Enemy, Weapon).
# 	•	Web applications (e.g., User, Post, Comment).
# 	•	Databases (e.g., Model, Table, Record).