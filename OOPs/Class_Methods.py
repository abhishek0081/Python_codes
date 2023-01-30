
class Person:
    Count_instance = 0;  # Class variable/ calss attribute
    def __init__(self,first_name,last_name,age):
        Person.Count_instance+=1;
        self.first_name = first_name;
        self.last_name = last_name;
        self.age = age;
    @classmethod
    def count_instances(cls):
        return f" You Have created  {cls.Count_instance} instances of {cls.__name__} class"
    def full_name(self):  # instance Method
        return f"{self.first_name}  {self.last_name}"
    def is_above18(self):  # instance method
        return self.age > 18;

# self represents object

p1 = Person("Abhishek","Kumar",21);
p2 = Person("Sujal","Choudhary",18);
# print(p1.full_name());
print(Person.count_instances())
# Person.Method_name();\
#  " You have created  4 instances for person class"  // using class methods
