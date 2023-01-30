#zip function

user_id = ['user 1','user 2','user 3','user 4'];
names = ['abhishek','sonu','jayant','robin'];
last_names = ['kumar','raj','yadav','yadav'];
# print(dict(zip(user_id,zip(names,last_names))));


#zip function part 2
l1 = [1,3,5,7]
l2 =[2,4,6,8]
l =[(1,2),(3,4),(5,6),(7,8)]

# l1,l2 = list(zip(*l))
# print(f"{list(l1)}\t{list(l2)}")
new_list =[]
# for pair in zip(l1,l2):
#     new_list.append(max(pair))

# print(new_list);
z= filter(lambda pair:(pair  for pair in zip(l1,l2)),zip(l1,l2));
for i in z:
    print(max(i));
l1,l2 = list(zip(*l));
print(l1);
print(l2)

# for pair in zip(l1,l2):
#     new_list.apeend(max(pair));

x = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)];

# a = int(input("Enter the size of list : "));
# print("\n");
# a = list(map(float, input("Enter the list numbers separated by comma ").strip().split(",")))[:a];
# print("User List: ", a);
# b = int(input("Enter the size of list : "));
# print("\n");
# b = list(map(float, input("Enter the list numbers separated by comma ").strip().split(",")))[:b];
# print("User List: ", b);
# c = int(input("Enter the size of list : "));
# print("\n");
# c = list(map(float, input("Enter the list numbers separated by comma ").strip().split(",")))[:c];
# print("User List: ", c);

print("Average of list Entered by User is : ",x(l1,l2),end="\n\n\t\t");
print("Average of list Entered by User is : ",x(l1,l2),end="\n");

def x(a,b):
    new_list = [sum(pair)/len(pair) for pair in zip(a,b)];
    return new_list;

print(x(l1,l2))
