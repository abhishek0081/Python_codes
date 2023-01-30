
#raise error example1
# abstract method
# NotImplementedError

class Animal:
    def __init__(self,name):
        self.name = name 

    def sound(self): # Abstract Method : JAVA
        raise NotImplementedError("Define this Method in subclasses")


class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name) 
        self.breed = breed
    def sound(self):
        return " Bhow - Bhow"
class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        return "Meow - Meow"

doggy = Dog("Khusi","Labroder");
cat = Cat("Khusi","Persian")
print(Cat.sound(cat))

# Abstract method came from JAVA