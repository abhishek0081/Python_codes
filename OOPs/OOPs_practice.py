class Laptop:
    discount_percent = 10
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+ " " +model_name
    def apply_discount(self):
        return f" Price after discount is : {self.price-self.price*self.discount_percent*0.01}"

# Laptop.discount_percent = 0;
lap1 = Laptop("HP","du3047tx",72000);
lap2 = Laptop("HP","du3049tx",80000);
lap2.discount_percent = 50;
# print(lap1.brand_name);
# print(lap2.laptop_name);
# print(lap1.apply_discount());
print(lap2.__dict__)
print(lap2.apply_discount());