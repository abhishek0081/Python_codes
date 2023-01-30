from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        """ THIS IS WRAPPPER FUNCTION """
        print("This is awesome Function ");
        return any_function(*args,**kwargs);
    return wrapper_function;

@decorator_function
def add(a,b):
    """THIS IS ADD FUNCTION """
    return a+b;

@decorator_function
def func(a):
    print(f"This is Function with Argument {a}");
func(5);

print(add(2,3));

print(add.__name__);