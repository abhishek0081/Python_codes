class A:
    def class_A_method(self):
        return "I\'m Just a Class A method"

    def hello(self):
        return "Hello from Class A";


class B:
    def class_B_method(self):
        return "I\'m Just a Class B method"

    def hello(self):
        return "Hello from Class B";

class C(A,B):
    pass

class C(B,A):
    pass

    
instance_a = A();
instance_c = C();
print(instance_c.hello())
print(instance_a.class_A_method());
# print(help(C))

print(C.mro())
print(C.__mro__)