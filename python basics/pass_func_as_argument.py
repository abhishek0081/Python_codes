#map
def square(a):
    return a**2;

l = list(range(1,11));
print(list(map(square,l)));

def my_map(func , l):
    new_list = [];
    for item in l:
        new_list.append(func(item));
    return new_list;

def my_map2(func , l):
    return [func(item) for item in l];

# print(my_map2(lambda a:a**3,l));
z = lambda func,l:{func(item) for item in l};
print(z(lambda a:a**4,l));
print(my_map2(lambda a:a**5,l));
