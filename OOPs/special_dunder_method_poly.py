# special Magic metho  eg : __init__
#operator Overlodaing
#Polymorphism

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand =brand;
        self.model_name = model_name;
        self.price = max(price,0)  # name mangling _classname__attributename
    def phone_name(Self):
        return f"{Self.brand} {Self.model_name}"

    #str #__repr__
    def __repr__(self):
        return f"Phone(\'{self.brand}\', \'{self.model_name}\', {self.price})"

    def __str__(self):
        return f"[{self.brand} {self.model_name}]"
    def __len__(self):
        return len(self.phone_name())
    def __add__(self,other):
        return f"{self.price+ other.price}"

    def __mul__(self,other):
        return self.price* other.price
class Smartphone(Phone):
    def __init__(self, brand, model_name, price,ram,internal_memory,rear_camera):
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    def phone_name(self):
        return f"{self.brand} {self.model_name} {self.ram}  and price is {self.price}";

phone1 = Phone("Samsung","A31",30000);
# print(repr(phone1))
# print(len(phone1))
# print(str(phone1))
phone2 = Smartphone("Samsung","A32",35000,"6 gb"," 128 gb","36 MP");
# print(phone2+phone1)
# print(phone2*phone1)
#  polymorphism
#  Eg :
# "abs" +"shek" = "abhishek"
# 2+ 3 = 5
# + operator  can contatinate two strings as well as two numbers as well thats called polymorphism
# operator overloading is also polymorphism example
# method overiding  is also a polymorphism

# here phone_name() working as polymorphism 
print(phone1.phone_name());

print(phone2.phone_name());