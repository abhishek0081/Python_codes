list.py
myList = [0, 3, 12, 8, 2]

print(5 in myList)
print(5 not in myList)
print(12 in myList)


#remove duplicates

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
rep = []
for i in myList:
    
    if i not in rep:
        rep.append(i)
print("The list with unique elements only:")
print(rep)