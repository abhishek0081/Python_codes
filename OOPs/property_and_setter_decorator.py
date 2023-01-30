class Phone:
    def __init__(self,brand,model_name,price):
        self.brand =brand;
        self.model_name = model_name;
        self._price = max(price,0);
        #self.complete_specification = f" {self.brand} {self.model_name} and price : {self._price}"
    @property
    def complete_specification(self):
        return f" {self.brand} {self.model_name} and price : {self._price}"
    #getter() or setter() method
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0);

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}");

    def full_name(self):
        return f"{self.brand} {self.model_name}";


phone1 = Phone("Samsung","A31",30000);
print(phone1.__dict__);
print(phone1.complete_specification);
phone1.price = 34000;
print(phone1.complete_specification);