# *     operator

#*args

# def total(a,b):
#     return a+b
# print(total(3,4,43,3453,3443,34))

def all_total(*args):
    # print(args)
    # print(type(args))
    total =0
    for num in args:
        total += num
    return total


print(all_total(3,34,max(34,56,678)))
myList = [10, 1, 8, 3, 5]
def func(*args):
    total =0
    for i in args:
        total += i
    return total

print(func(*myList))

myList = [10, 1, 8, 3, 5]
length = len(myList)
for i in range(length // 2):
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]

print(myList)
print(length // 2)