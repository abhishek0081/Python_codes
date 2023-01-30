from functools import wraps

def only_data_type(data_type):
    def decorator(function):
        @wraps(function)
        def wrapper_function(*args,**kwargs):
            if all((type(arg)==data_type)for arg in args):
                return function(*args,**kwargs);
            return "INVALID ARGUMENTS"
        return wrapper_function
    return decorator
@only_data_type(str)
def string_join(*args):
    string = "";
    for i in args:
        string+= i;
    return string;


print(string_join("Kuakmr","abhishek"));

        
