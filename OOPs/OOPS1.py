#OBJECTIVES
# WHAT IS  INIT METHOD # constructor
# WHAT ARE ATTRIBUTES
# HOW TO CRESTE OUR OBJECT
#HOW TO WRITE A CLASS
#WHAT IS CLASS?
 


class Person: # to define our class  # convention first letter of user defined class must be Capital
    def __init__(self,first_name,last_name,age):  # first_name, last_name,age is attribute of person
        # create instance vaariables  using attributes
        print("init method / constructor method called ......")
        self.person_first_name = first_name  # instance variable declared
        self.last_name = last_name
        self.age = age


# self represents object
p1= Person("Abhishek","Kumar",21);
p2 = Person("Sujal","Choudhary",18);
print(p1.person_first_name);
print(p2.person_first_name);
