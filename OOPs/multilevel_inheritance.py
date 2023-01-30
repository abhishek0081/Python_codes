
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
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    def full_name(self):
        return f"{self.brand} {self.model_name} {self.ram}  and price is {self.price}";

class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera,front_camera,processor,display):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
        self.processor = processor
        self.disply = display
    def full_name(self):
        return f"{self.brand} {self.model_name} ram is  : {self.ram}  and price is {self.price} processor is : {self.processor}";
samsung1 = FlagshipPhone("samsung","A31",30000,"6gb","128gb","32 mp","16 mp","Exynos 9825","Amoled");
samsung2 = Smartphone("samsung","A31",30000,"6gb","128gb","32 mp");
print(samsung1.full_name());
# print(samsung.__dict__)
print(samsung2.full_name())

#  Method Resolution Order 

###### MRO  #########

# print(help(FlagshipPhone))


# isinsstance :
# print(isinstance(samsung2,FlagshipPhone));
# print(isinstance(samsung2,Phone));


#issubclass

print(issubclass(Smartphone,FlagshipPhone))
print(issubclass(Smartphone,Phone))
print(issubclass(FlagshipPhone,Smartphone))