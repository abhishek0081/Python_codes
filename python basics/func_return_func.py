def outer_func():
    def inner_func():
        print("Inside inner func ");
    return inner_func;

var = outer_func();
# var();

def outer_func2(msg):
    def innner_fun2():
        print(f"message is {msg}");
    return innner_fun2;

var2 =outer_func2("hi here is abhishek!");
var2();