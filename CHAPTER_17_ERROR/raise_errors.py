def add(a,b):
    if (type(a) is int and  type(b) is int):
        return a+b
    raise TypeError(" OOPs you entered a wrong data type")
print(add("2","3"))
