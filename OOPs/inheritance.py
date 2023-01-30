
class Phone:
    def __init__(self,brand,model_name,price):
        self.brand =brand;
        self.model_name = model_name;
        self.price = max(price,0)  # name mangling _classname__attributename

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number}........");

    def full_name(self):
        return f"{self.brand} {self.model_name}";

class Smartphone(Phone):
    def __init__(self, brand, model_name, price,ram,internal_memory,rear_camera):
        super().__init__(brand, model_name, price)
    # def __init__(self, brand, model_name, price,ram,internal_memory,rear_camera):
        # Phone.__init__(self,brand,model_name,price) # uncommon way 
        # super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

        
smartphone = Smartphone("Samsung Galaxy","A31",30000,"6gb","64gb","32mp");

print(smartphone.full_name())