#map_function
number = list(range(1,11));


def square(*args):
    temp = [];
    for i in args:
        temp.append(i**2);
    return temp;
# print(square(*number))
# z = list(map(lambda a:a**2,number))
# print(z)
# sqaures_new =[i**2 for i in number]
# print(sqaures_new)

# new_list = []
# for num in number:
#     new_list.append(square(num))

# print(new_list)

names = ['abc','abxc','abxcd'];

length = map(len,names);
print(length);
for i in length:
    print(i);

# for j in length:
#     print(j)
z= map(lambda a:a**2,number);
# f = [i for i in z];
for i in z:
    print(i);

f = map(len,names);
for i in f:
    print(i);

