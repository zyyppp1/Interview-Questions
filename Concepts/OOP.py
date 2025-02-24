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
# We use abstract classes to enforce certain methods in child classes.
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract base class (ABC)
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        # Abstract method that must be implemented in subclasses
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

# animal = Animal("Unknown")  # ❌ Cannot instantiate an abstract class
dog = Dog("Buddy")
print(dog.make_sound())  # ✅ Woof! Woof!