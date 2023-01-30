
def average_finder(l1,l2):
    for i in l1,l2:
        average =(l1[i] +l2[i])/(len(l1)+len(l2))/2
    return average

a = [1,2,3]
b = [4,5,6]
print(average_finder(a,b))