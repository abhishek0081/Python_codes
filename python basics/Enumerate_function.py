#We use Enumerate function  with for looop to track position of our parameter 
#Item in itertable

# #doing this without Enumerate Function
names =['abhishek','sujal','sonu','jayant'];
# #o  ---> 'abhishek
# #1  ---> 'suajl'

# pos =0
# for name in names:
#     print(f"{pos} -----> {name}")
#     pos +=1

#With Enumerate Function:
# for pos,name in enumerate(names):
#     print(f"{pos} -----> {name}")


def find_position(l,target):
    for pos,name in enumerate(l):
        if name == target:
            return pos;
    return -1;

# print(find_position(names,'abhi'))

# def find_position(l,target):
#     for pos,name in enumerate(l):
#         if name == target:
#             return pos 
#     return -1


print(find_position(names,"abhis"));

    
