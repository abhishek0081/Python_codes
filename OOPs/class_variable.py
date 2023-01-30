# Class Variable
# Circle
# area
# Cicumference
class Circle :
    pi = (22/7);
    def __init__(self,radius):
        self.radius = radius;
    def circumference(self):
        return f"Circumference of circle of given radius {self.radius} is : {2*self.radius*Circle.pi}";
    def Area(self):
        return f" Area of the circle with given radius as {self.radius} is : {4*Circle.pi*self.radius**3}"
    
c = Circle(4);
c1 = Circle(18);
print(c.circumference());
print(c.Area());