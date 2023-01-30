# Decorators  ---- Enhances the functionality of other functions ;
# @used for decorators

#this is awesome fucntion

def Decorater_function(any_function):
    def wrapper_function():
        print("this is awesome fucntion");
        any_function();
    return wrapper_function;

@Decorater_function  #shortcut
def func1():
    print('this is function 1:');

func1();
@Decorater_function 
def func2():
    print('this is fucntion 2 : ');
func2();
# func1();
# fun2();
# var = Decorater_function(func1);
# var();

def decorater_function(any_function):
    def wrapper_function():
        print("This is Awesome Fucntion");
        any_function();
    return wrapper_function;

# var = decorater_function(func2)
# var();