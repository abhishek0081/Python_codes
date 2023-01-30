import time

from functools import wraps

def calculate_time(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        t1 = time.time();
        print(f"Executing .......{any_function.__name__}");
        returned_valued =  any_function(*args,**kwargs);
        t2 = time.time();
        print(f"This function took {t2-t1} sec");
        return returned_valued
    return wrapper_function;




t1 = time.time();
@calculate_time
def to_power(x):
    def calc_power(n):
        return n**x;
    return calc_power;

cube = to_power(977);
print(cube(598));
# t2 = time.time();
# print(f"This function took {t2-t1} sec");
@calculate_time
def add(a,b):
    """THIS IS ADD FUNCTION """
    return a+b;

print(add(12,67))
