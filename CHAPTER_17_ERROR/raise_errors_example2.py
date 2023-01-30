# rasie Errors example 2
class Mobile:
    def __init__(self,name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError("New Mobile should be object of Mobile class")
        

oneplus = Mobile("One Plus 6t");
samsung = "samsung galaxy A31"
mobostore = MobileStore()
print(mobostore.mobiles)
# mobostore.add_mobile(samsung)
mobostore.add_mobile(oneplus)
print(mobostore.mobiles[0].name)