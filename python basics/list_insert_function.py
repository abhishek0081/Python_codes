# myList = [] # creating an empty list

# for i in range(5):
#     myList.append(i + 1)

# print(myList)
myList = [] # creating an empty list

for i in range(5):
    myList.insert(i,i + 1)

print(myList)



#new things


#del function loopping with append function
# step 1
beatles =[]

print("Step 1:", beatles)

# step 2
beatles.append("Jhon Lenon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
user1,user2 = input("Enter  the band list seperated by comma  : ").split(",")
for i in range(1):
    beatles.append(user1)
    beatles.append(user2)
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))




#sorting by swaping using loop

myList = [8, 10, 6, 2, 4] # list to sort
swapped = True # it's a little fake - we need it to enter the while loop

while swapped:
    swapped = False # no swaps so far
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True # swap occured!
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print(myList)


#reverse method

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst) # outputs: [4, 2, 1, 3, 5]



#sort methods

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst) # outputs: [1, 2, 3, 4, 5]