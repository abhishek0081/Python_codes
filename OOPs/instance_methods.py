#instance method

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name;
        self.last_name = last_name;
        self.age = age;
    def full_name(self):  # instance Method
        return f"{self.first_name}  {self.last_name}"
    def is_above18(self):
        return self.age > 18;

p1 = Person("Abhishek","Kumar",21);
p2 = Person("Sujal","Choudhary",18);
print(p1.full_name());
print(p2.full_name());   #  Person.full_name(p2);
print(Person.full_name(p2));
print(p2.is_above18())
