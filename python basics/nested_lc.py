# nested_comp = [[i for i in range(1,4)] for j in range(1,4)]
# print(nested_comp)

# new_list = []
# for j in range(3):
#     new_list.append([1,2,3])

nums=list(range(1,11))
new_list =[]
for i in nums:
    if i%2 == 0:
        new_list.append(i**2)
    else:
        new_list.append(-i)
print(new_list)

new_list2 = [i**2 if(i%2 ==0 ) else -i for i in nums]
print(new_list2)