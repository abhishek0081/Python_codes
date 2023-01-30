
# def average_finder(*args):
#     new_list =[]
#     for pair in zip(*args):
#         new_list.append(sum(pair)/len(pair))

#     return new_list

# a = [1,2,3]
# b = [4,5,6]
# c = [2,5,6]]


# print(average_finder(a,b,c))
a = int(input("Enter the size of list : "));
print("\n");
a = list(map(float, input("Enter the list numbers separated by comma ").strip().split(",")))[:a];
print("User List: ", a);
b = int(input("Enter the size of list : "));
print("\n");
b = list(map(float, input("Enter the list numbers separated by comma ").strip().split(",")))[:b];
print("User List: ", b);
c = int(input("Enter the size of list : "));
print("\n");
c = list(map(float, input("Enter the list numbers separated by comma ").strip().split(",")))[:c];
print("User List: ", c);
#  in one linea

# anonymous = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
# print(anonymous(a,b,c))
# args = ([],[])

x = lambda *args:[sum(pair)/len(pair)for pair in zip(*args)];
    
    
# print(x(a,b,c))

# def average_finder(*args):
#     temp =[]
#     for pair in zip(*args):
#         temp.append(sum(pair)/len(pair))

#     return temp


# print(average_finder(a,b,c))
# y = [2,5,6]
# y.insert(1,3)
# print(y);

x =[4,100,100];

new_list = [max(pair) in x for pair in zip(a,b,c)];
print(new_list);
z = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)];

# a = [1,2,3,4];
# b = [6,5,32,33];
# c = [7,4,53,2,4];

# for i in z:
    # print(i);
print(z(a,b,c));
