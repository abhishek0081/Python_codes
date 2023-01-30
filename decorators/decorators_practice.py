from functools import wraps

def print_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print(f"You are calling {any_function.__name__} function");
        print(f"{any_function.__doc__}");
        return any_function(*args,**kwargs);
    return wrapper_function;

@print_function
def add(a,b):
    '''This function takes two values and add it'''
    return a+b;

print(add(4,5));
