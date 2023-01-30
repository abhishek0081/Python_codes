#filter function

def is_even(a):
    return a%2 ==0

numbers = list(range(1,12))


lambda a :a%2 ==0
evens  = filter(lambda a :a%2 ==0,numbers)
for i  in  evens:
    print(i)

evens =[i for i in numbers if i%2 ==0]
print(evens)