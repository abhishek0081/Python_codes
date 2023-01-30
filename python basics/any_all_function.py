#any ,all function
numbers1 = [2,4,6,58,101,12]
numbers2 = [1,3,5,7,9,11]
# z = lambda *args:("even" if( all(i%2 == 0 , j%2 ==0) for i,j in pair) else "odd" for pair in zip(*args))
# iter(numbers1)
# h = lambda *numbers2:[i if(i%2 == 0)else "odd" for i in numbers2]
# u = map(h,*numbers2)
# for j in u:
#     print(u(numbers1))

# print(all([num%2 == 0 for num in numbers1]))
# print(([num%2 == 0 for num in numbers1]))
# print(any([num%2 == 0 for num in numbers1]))


#any all fucntion
def my_sum(*args):
    #args
    if all([(type(arg)==int or type(arg)==float)for arg in args]):
        total= 0
        for num in args:
            total+=num
        return total
    else:
        return "Wrong Input"
name =['abhishek kumar','sujal choudhary']
# print(my_sum(2,3,45,6,67,7.9,*numbers1,*numbers2,name))

z = lambda args:[ i%2==0 if((i%2==0))else i%2==0 for i in args];
print((all(z(numbers1))));
        
