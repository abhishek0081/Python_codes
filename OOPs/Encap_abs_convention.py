# Encapsulation
# Abstraction
# some special naming convention
# Mangling  ,__name() not a convention

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand =brand;
        self.model_name = model_name;
        self.__price = price  # name mangling _classname__attributename

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}");

    def full_name(self):
        return f"{self.brand} {self.model_name}";


l = [3,5,6,1,0];
l.sort() # tim sort
print(l)

# naming convention  _name  # convention for private name
# __name__  # dunder  ,magic methods

phone1 = Phone("Samsung","J7 Prime",7500);
# print(phone1.__price)
phone1._price =50;
# print(phone1.__price)
print(phone1.__dict__)