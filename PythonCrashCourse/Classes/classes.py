class Dog:
    """A simple class to model dogs"""
    def __init__(self,name,age):
        """Initialize the name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        return f"{self.name} is now sitting."

    def roll_over(self):
        return f"{self.name} rolled over!"


#A new instance
my_dog = Dog("Bobby",11)

#Get attributes
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's age is {my_dog.age}.")

#Call the methods
print(my_dog.sit())
print(my_dog.roll_over())

print("\n\nAnother Dog:\n\n")

#Another instance
another_dog = Dog("Holly",2)

#Attributes
print(f"My dog's name is {another_dog.name}.")
print(f"My dog's age is {another_dog.age}.")

#Methods
print(another_dog.sit())
print(another_dog.roll_over())