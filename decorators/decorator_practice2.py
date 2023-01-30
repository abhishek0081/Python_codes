#only int allow

from functools import wraps

def only_int(func):
    @wraps(func)
    def wrapper_function(*args,**kwargs):
        if all((type(arg)==int or type(arg)==float)for arg in args):
            return func(*args,**kwargs);
        return "INVALID ARGUMENTS"
    return wrapper_function


@only_int
def add_all(*args):
    total =0
    for i in args:
        total+=i
    return total

print(add_all(2,5,7,8,8.6));